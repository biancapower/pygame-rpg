import pygame

from asset import *
from square import *


grass = pygame.image.load('town_rpg_pack/graphics/grass-tile.png')

tiles = pygame.image.load('town_rpg_pack/graphics/transparent-bg-tiles.png')


#   nonexistent
# B background
# X obstacle
# O object
# F foreground (above player)
classification = [
  'X  X     FFFFFF    F  ',
  'XXXX FFF XXXXXX   FFF ',
  '    BFFFFXXXXXX   XXX ',
  '    BXXXFXXXXXXXXXXXX ',
  '    BXXXXXXXXXXXXXXXXB',
  '  O BXXXXXXXXXXXX XXXB',
  ' BBBBXXXXXXXXXXXX XXXB',
  ' BBB  XXXBBBBBBBB XXXB',
  ' BBB OBOOO X    B XXXB',
  '    B B    X    B     ',
  'XXX X XXXXXXX BBBBBBBB ',
  'XXX X XXXXXXX   B      ',
  '          XXX   B      ',
  'XBBBBXXXX XXX          ',
  'XXXXXXXXXX             ',
  'XXXXXX  X              ',
  'XXXXXX                 ',
  '                       ',
]




world = []
for y in range(0, tiles.get_height(), HEIGHT):
    world_row = []
    for x in range(0, tiles.get_width(), WIDTH):
        square = Square()

        grass_tile = Asset(grass, x, y)
        
        square.graphics.append(grass_tile)
        if classification[y//HEIGHT][x//WIDTH] != ' ':
            new_tile = tiles.subsurface( (x, y, WIDTH, HEIGHT) )
            new_tile = Asset(new_tile, x, y)

            square.graphics.append(new_tile)

        world_row.append(square)
    world.append(world_row)

player_sheet = pygame.image.load('town_rpg_pack/graphics/hero.png')

WORLD_WIDTH = len(world[0]) * WIDTH * SCALE
WORLD_HEIGHT = len(world) * HEIGHT * SCALE
