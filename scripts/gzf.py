from enum import Enum
import struct
from PIL import Image

from helper import get_point_sequence


class GZFImageFormat(Enum):
  L4 = 8
  L8 = 6


class GZFEntry:
  char: str
  top: int
  left: int
  blank_width: int
  height: int
  image_id: int

  def __init__(
      self,
      data_or_char: bytes | bytearray | str,
      top: int = 0,
      left: int = 0,
      blank_width: int = 2,
      height: int = 15,
      image_id: int = 0,
  ) -> None:
    if isinstance(data_or_char, str):
      self.char = data_or_char

    elif isinstance(data_or_char, bytes) or isinstance(data_or_char, bytearray):
      assert len(data_or_char) == 0x0c
      char, height, image_id, blank_width, left, top = struct.unpack("<IHHHBB", bytes(data_or_char))
      self.char = chr(char)

    else:
      raise ValueError("Invalid data type")

    self.top = top
    self.left = left
    self.blank_width = blank_width
    self.height = height
    self.image_id = image_id

  def __json__(self):
    return {
        "char": self.char,
        "top": self.top,
        "left": self.left,
        "width": self.blank_width,
        "height": self.height,
        "image_id": self.image_id
    }

  def get_bytes(self) -> bytes:
    return struct.pack("<IHHHBB", ord(self.char), self.height, self.image_id, self.blank_width, self.left, self.top)


class GZFImage:
  format: GZFImageFormat
  offset: int
  width: int
  height: int
  image: Image.Image

  def __init__(
      self,
      header: bytes | bytearray,
      data: bytes | bytearray,
      format: GZFImageFormat,
  ) -> None:
    self.format = format
    self.offset, self.width, self.height = struct.unpack("<IHH", header)

    image_data_len = self.width * self.height // (2 if format == GZFImageFormat.L4 else 1)
    image_data = bytearray(data[self.offset:self.offset + image_data_len])
    image = Image.new("L", (self.width, self.height))
    for i, (x, y) in enumerate(get_point_sequence(self.width, self.height)):
      if format == GZFImageFormat.L4:
        byte = image_data[i // 2]
        alpha = (byte & 0x0F if i % 2 == 0 else byte >> 4) << 4
        if alpha == 0xF0:
          alpha = 0xFF
      else:
        alpha = image_data[i]
      image.putpixel((x, y), (alpha))
    self.image = image

  def __json__(self):
    return {
        "offset": self.offset,
        "width": self.width,
        "height": self.height,
    }

  def get_bytes(self) -> bytes:
    return struct.pack("<IHH", self.offset, self.width, self.height)

  def get_image_bytes(self) -> bytes:
    image_data = bytearray()
    for i, (x, y) in enumerate(get_point_sequence(self.width, self.height)):
      alpha = self.image.getpixel((x, y))
      if self.format == GZFImageFormat.L4:
        if i % 2 == 0:
          image_data.append(alpha >> 4)
        else:
          image_data[-1] = (image_data[-1] & 0x0F) | (alpha >> 4 << 4)
      else:
        image_data.append(alpha)
    return bytes(image_data)


class GZF:
  version: int
  image_header_offset: int
  image_len: int
  entry_len: int
  image_num: int
  entry_num: int
  unk2: int
  format: GZFImageFormat
  font_size: int
  unk4: int
  unk5: int
  tile_width: int
  tile_height: int
  images: list[GZFImage]
  entries: list[GZFEntry]

  def __init__(
      self,
      data: bytes | bytearray,
  ) -> None:
    self.data = bytearray(data)

    assert self.data[0x00:0x04] == b"GZFX"
    self.version, self.image_header_offset, self.image_len, self.entry_len, unk1 = struct.unpack(
        "<IHHHH", self.data[0x04:0x10])
    self.image_num, self.entry_num, unk2, format = struct.unpack("<IIII", self.data[0x10:0x20])
    self.font_size, self.unk4, self.unk5, self.tile_width, self.tile_height, unk8, unk9 = struct.unpack(
        "<HHHHHHI", self.data[0x20:0x30])

    assert self.image_len == 0x08
    assert self.entry_len == 0x0C
    assert unk1 == 0
    assert unk2 == 0xff0a
    assert unk8 == 0
    assert unk9 == 0

    self.format = GZFImageFormat(format)

    self.images: list[GZFImage] = []
    for i in range(self.image_num):
      offset = self.image_header_offset + i * self.image_len
      header = self.data[offset:offset + self.image_len]
      self.images.append(GZFImage(header, self.data, self.format))

    entry_header_offset = self.image_header_offset + self.image_num * self.image_len
    self.entries: list[GZFEntry] = []
    for i in range(self.entry_num):
      offset = entry_header_offset + i * self.entry_len
      entry_data = self.data[offset:offset + self.entry_len]
      self.entries.append(GZFEntry(entry_data))

    empty_data = self.data[entry_header_offset + self.entry_num * self.entry_len:self.images[0].offset]
    assert all(map(lambda x: not x, empty_data))

  def __json__(self):
    return {
        "version": self.version,
        "image_header_offset": self.image_header_offset,
        "image_len": self.image_len,
        "entry_len": self.entry_len,
        "image_num": self.image_num,
        "entry_num": self.entry_num,
        "format": self.format.value,
        "font_size": self.font_size,
        "unk4": self.unk4,
        "unk5": self.unk5,
        "tile_width": self.tile_width,
        "tile_height": self.tile_height,
        "images": self.images,
        "entries": self.entries,
    }

  def get_bytes(self) -> bytes:
    header = struct.pack(
        "<IHHHH",
        self.version,
        self.image_header_offset,
        self.image_len,
        self.entry_len,
        0,
    ) + struct.pack(
        "<IIII",
        self.image_num,
        self.entry_num,
        0xff0a,
        self.format.value,
    ) + struct.pack(
        "<HHHHHHI",
        self.font_size,
        self.unk4,
        self.unk5,
        self.tile_width,
        self.tile_height,
        0,
        0,
    )

    entries_data = bytearray()
    for entry in self.entries:
      entries_data += entry.get_bytes()

    images_data = bytearray()
    images_header_data = bytearray()
    current_pos = 0x30 + self.image_num * self.image_len + self.entry_num * self.entry_len
    for image in self.images:
      padding = (0x80 - current_pos % 0x80) % 0x80
      current_pos += padding
      image.offset = current_pos
      images_header_data += image.get_bytes()
      image_data = image.get_image_bytes()
      images_data += bytes([0] * padding) + image_data
      current_pos += len(image_data)

    return b"GZFX" + header + images_header_data + entries_data + images_data
