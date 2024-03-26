import os
import re
import struct

COMMANDS_LENGTH = {
    0x08: 2,
    0x0E: 2,
    0x0F: 2,
    0x11: 1,
    0x19: 4,
}

COMMANDS_NEED_ALIGN = [
    0x08,
    0x0E,
    0x0F,
    0x19,
]


def bytes_to_string(bytes_data: bytes) -> str:
  chars = struct.unpack("<%dH" % (len(bytes_data) // 2), bytes_data)
  output = ""
  i = 0
  while i < len(chars):
    char = chars[i]
    if char == 0x7f:
      i += 1
      char = chars[i]
      if char == 0:
        i = len(chars)
        continue
      if char == 1:
        output += "<br>"
        i += 1
        continue
      if char == 2:
        output += "<hr>"
        i += 1
        continue
      if char == 0x15:
        if i % 2 == 0:
          i += 1
        if chars[i + 1] == 0xffff:
          assert chars[i + 2] == 0xffff
          output += "</span>"
          i += 2
        else:
          output += "<span class=\"color-"
          i += 1
          output += hex(chars[i])[2:].upper().zfill(4)
          output += "\">"
        if i % 2 == 0:
          i += 1
        i += 1
        continue
      if char == 0x16:
        output += "<ruby>"
        i += 1
        rt = ""
        while chars[i] != 0:
          rt += chr(chars[i])
          i += 1
        i += 1
        while i + 1 < len(chars) and not (chars[i] == 0x7F and chars[i + 1] == 0x17):
          output += chr(chars[i])
          i += 1
        output += "<rt>" + rt + "</rt></ruby>"
        i += 2
        continue
      output += "[" + hex(char)[2:].upper().zfill(4)
      if char in COMMANDS_NEED_ALIGN:
        if i % 2 == 0:
          i += 1
        for i in range(i + 1, i + 1 + COMMANDS_LENGTH[char], 2):
          output += "," + hex(chars[i])[2:].upper().zfill(4)
        i += 1
      elif char in COMMANDS_LENGTH:
        for i in range(i + 1, i + 1 + COMMANDS_LENGTH[char]):
          output += "," + hex(chars[i])[2:].upper().zfill(4)
      output += "]"
    elif char < 32:
      output += "\\x" + hex(char)[2:].zfill(2)
    elif 0xe000 < char < 0xe07f or char == 0xffff:
      output += "\\u" + hex(char)[2:].zfill(4)
    else:
      output += chr(char)
    i += 1
  return output


def string_to_bytes(string_data: str) -> bytes:
  chars = []
  i = 0
  while i < len(string_data):
    c = string_data[i]
    if c == "[":
      end = string_data.index("]", i + 2)
      codes = [int(i, 16) for i in string_data[i + 1:end].split(",")]
      if codes[0] in COMMANDS_NEED_ALIGN:
        chars.append(0x7F)
        chars.append(codes[0])
        if len(chars) % 2 == 1:
          chars.append(0)
        for j in codes[1:]:
          chars.append(j)
          chars.append(0)
      else:
        chars.append(0x7F)
        chars += codes
      i = end + 1
    elif c == "<":
      end = string_data.index(">", i + 2)
      tag = string_data[i + 1:end]
      if tag == "br":
        chars.append(0x7F)
        chars.append(0x01)
      elif tag == "hr":
        chars.append(0x7F)
        chars.append(0x02)
      elif tag.startswith("span "):
        colorStart = tag.index("color-") + 6
        tagClass = int(tag[colorStart:colorStart + 4], 16)
        chars.append(0x7F)
        chars.append(0x15)
        if len(chars) % 2 == 1:
          chars.append(0)
        chars.append(tagClass)
        chars.append(0)
      elif tag == "/span":
        chars.append(0x7F)
        chars.append(0x15)
        if len(chars) % 2 == 1:
          chars.append(0)
        chars.append(0xFFFF)
        chars.append(0xFFFF)
      elif tag == "ruby":
        chars.append(0x7F)
        chars.append(0x16)
        rtStart = string_data.index("<rt>", end)
        rtEnd = string_data.index("</rt>", rtStart + 4)
        rt = string_data[rtStart + 4:rtEnd]
        ruby = string_data[end + 1:rtStart]
        end = string_data.index("</ruby>", rtEnd + 5) + 6
        for j in rt:
          chars.append(ord(j))
        chars.append(0)
        for j in ruby:
          chars.append(ord(j))
        chars.append(0x7F)
        chars.append(0x17)
      i = end + 1
    else:
      chars.append(ord(c))
      i += 1
  chars.append(0x7F)
  chars.append(0x00)
  bytes_data = struct.pack("<%dH" % len(chars), *chars)
  return bytes_data


def convert_gmsg_to_markdown(gmsg_path: str, markdown_path: str):
  with open(gmsg_path, "rb") as reader:
    data = reader.read()
  entry_num, start_pos = struct.unpack("<II", data[0x0C:0x14])

  with open(markdown_path, "w", encoding="utf-8") as writer:
    writer.write(
        "<style> .color-0001 { color: #39BE39; }  .color-0002 { color: #FF6942; }  .color-0003 { color: #FF9E18; } </style>\n| ID | TEXT |\n| --- | --- |\n"
    )
    for i in range(entry_num):
      id, unknown, offset, length = struct.unpack("<4I", data[start_pos + i * 0x10:start_pos + i * 0x10 + 0x10])
      bytes_data = data[offset:offset + length]
      string_data = bytes_to_string(bytes_data)
      writer.write(f"| 0x{id:04x} | {string_data} |\n")


def convert_markdown_to_gmsg(gmsg_path: str, markdown_path: str, output_path: str):
  PATTERN = re.compile(r"^\| 0x([0-9a-fA-F]+) \| ([^\|]+) \|$", re.M)
  with open(markdown_path, "r", encoding="utf-8") as reader:
    text = {int(i[0], 16): i[1] for i in PATTERN.findall(reader.read())}
  assert len(text) <= 2182

  with open(gmsg_path, "rb") as reader:
    data = bytearray(reader.read())

  entry_num, start_pos = struct.unpack("<II", bytes(data[0x0C:0x14]))
  new_offset, = struct.unpack("<I", bytes(data[start_pos + 0x08:start_pos + 0x0C]))
  for i in range(entry_num):
    id, unknown, offset, length = struct.unpack("<4I", bytes(data[start_pos + i * 0x10:start_pos + i * 0x10 + 0x10]))
    assert id in text

    string_data = text[id]
    bytes_data = string_to_bytes(string_data)

    new_length = len(bytes_data)
    data[new_offset:new_offset + new_length] = bytes_data
    new_header = struct.pack("<4I", id, unknown, new_offset, new_length)
    data[start_pos + i * 0x10:start_pos + i * 0x10 + 0x10] = new_header
    new_offset += new_length
    if new_offset % 4 > 0:
      new_offset += 4 - new_offset % 4

  with open(output_path, "wb") as writer:
    writer.write(data)


if __name__ == "__main__":
  # convert_gmsg_to_markdown("files/main.gmsg", "texts/ja/main.md")
  for language in os.listdir("texts/"):
    if language == "ja" or not os.path.isdir(f"texts/{language}"):
      continue
    os.makedirs(f"out/{language}", exist_ok=True)
    convert_markdown_to_gmsg("files/main.gmsg", f"texts/{language}/main.md", f"out/{language}/main.gmsg")
