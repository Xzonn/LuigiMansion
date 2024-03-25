# Reference: https://github.com/IcySon55/Kuriimu/blob/master/src/Cetera/Image/Common.cs
# Licence: GPL-3.0
# https://raw.githubusercontent.com/IcySon55/Kuriimu/master/LICENSE.md

from enum import Enum
import math
from typing import Any, Generator

class Orientation(Enum):
  Default = 0
  HorizontalFlip = 1
  Rotate90 = 2
  Transpose = 3
  TransposeTile = 0x10000

def ZOrderX(tile_size: int, count : int) -> int:
  div = tile_size // 2
  x_in = count // div & div
  while div > 1:
    div = div // 2
    x_in |= count // div & div
  return x_in


def ZOrderY(tile_size: int, count: int) -> int:
  div = tile_size
  div2 = tile_size // 2
  y_in = count // div & div2
  while div2 > 1:
    div = div // 2
    div2 = div2 // 2
    y_in |= count // div & div2
  return y_in


def get_point_sequence(width: int, height: int, orientation: Orientation = Orientation.Default, tile_size: int = 8, z_order: bool = True) -> Generator[tuple[int, int], Any, None]:
  stride_width, stride_height = (width + 7) & ~7, (height + 7) & ~7
  if z_order:
    tile_size = 2 << int(math.log(((tile_size + 7) & ~7) - 1, 2))
  pow_tile_size = int(tile_size**2)
  stride = stride_width

  for i in range(stride_width * stride_height):
    x_out, y_out, x_in, y_in = 0, 0, 0, 0
    if z_order:
      x_out = (i // pow_tile_size % (stride // tile_size)) * tile_size
      y_out = (i // pow_tile_size // (stride // tile_size)) * tile_size
      x_in = ZOrderX(tile_size, i)
      y_in = ZOrderY(tile_size, i)

    if orientation == Orientation.Default:
      yield (x_out + x_in, y_out + y_in)
    elif orientation == Orientation.HorizontalFlip:
      yield (stride - 1 - (x_out + x_in), y_out + y_in)
    elif orientation == Orientation.Rotate90:
      yield (y_out + y_in, stride - 1 - (x_out + x_in))
    elif orientation == Orientation.Transpose:
      yield (y_out + y_in, x_out + x_in)
    elif orientation == Orientation.TransposeTile:
      yield (x_out + y_in, y_out + x_in)
    else:
      raise ValueError("Invalid orientation")
