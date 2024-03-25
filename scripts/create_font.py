import os
import re
from PIL import Image, ImageDraw, ImageFont
import requests
from gzf import GZF, GZFEntry

with open("files/main.gzf", "rb") as reader:
  data = reader.read()

gzf = GZF(data)

entries: dict[str, GZFEntry] = {}
old_entries: dict[str, GZFEntry] = {}
for item in gzf.entries:
  old_entries[item.char] = item

with open("texts/zh_Hans/main.md", "r", encoding="utf-8") as reader:
  text = reader.read()
  characters = sorted(set(" 　©" + re.sub(r"\s", "", text)))

SCALE = 1

x, y = 1, 0
tile_width = gzf.tile_width
tile_height = gzf.tile_height
image_width, image_height = 1024, 768

new_entries = []
new_image = Image.new("L", (image_width * SCALE, image_height * SCALE))

if not os.path.exists("out/HYMaQiDuo-75W.ttf"):
  with open("out/HYMaQiDuo-75W.ttf", "wb") as writer:
    writer.write(requests.get("https://hellofonts.oss-cn-beijing.aliyuncs.com/%E6%B1%89%E4%BB%AA%E7%8E%9B%E5%A5%87%E6%9C%B5/9.00.00/HYMaQiDuo-75W.ttf").content)

font = ImageFont.truetype("out/HYMaQiDuo-75W.ttf", 15 * SCALE)
for char in characters:
  if (ord(char) < 0x4E00 or ord(char) >= 0xE000) and char in old_entries:
    entry = old_entries[char]
    if char in "“”":
      entry.blank_width = 2
      entry.height = 16
    tile = gzf.images[entry.image_id].image.crop((
        entry.left * tile_width + 1,
        entry.top * tile_height + 1,
        entry.left * tile_width + tile_width + 1,
        entry.top * tile_height + tile_height + 1,
    ))
    if SCALE != 1:
      tile = tile.resize((tile_width * SCALE, tile_height * SCALE), Image.Resampling.LANCZOS)
  else:
    entry = GZFEntry(char, 0, 0, 2, 16, 0)
    tile = Image.new("L", (tile_width * SCALE, tile_height * SCALE), 0)
    draw = ImageDraw.Draw(tile)
    draw.text(
        (10 * SCALE, 16 * SCALE),
        char,
        255,
        font,
        "ms",
        stroke_width=2 * SCALE,
        stroke_fill=128,
    )

  entry.left = x // tile_width
  entry.top = y // tile_height
  new_entries.append(entry)
  new_image.paste(tile, (x * SCALE, y * SCALE))
  x += tile_width
  if x + tile_width > image_width:
    x = 1
    y += tile_height

new_image.save("out/test.png")

gzf.entry_num = len(new_entries)
gzf.entries = new_entries[:gzf.entry_num]
gzf.images[0].image = new_image
gzf.images[0].width = image_width
gzf.images[0].height = image_height

with open("out/main.gzf", "wb") as writer:
  writer.write(gzf.get_bytes())
