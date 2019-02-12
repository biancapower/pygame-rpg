import pygame

from asset import *
from square import *
from obstacle import *
from foreground import *
from background import *
from object import *

grass = pygame.image.load('town_rpg_pack/graphics/grass-tile.png')

tiles = pygame.image.load('town_rpg_pack/graphics/transparent-bg-tiles.png')


#   nonexistent
# B background
# X obstacle
# O object
# F foreground (above player)
classification = [
  'X XX     FFFFFF    F  ',
  'XXXX FFF XXXXXX   FFF ',
  '    BFFFFXXXXXX   XXX ',
  '    BXXXFXXXXXXXXXXXX ',
  '    BXXXXXXXXXXXXXXXXB',
  '  O BXXXXXXXXXXXX XXXB',
  ' BBBBXXXXXXXXXXXX XXXB',
  ' BBB XXXXBBBBBBBB XXXB',
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
        
        square.layers.append(grass_tile)

        obj_type = classification[y//HEIGHT][x//WIDTH]
        if obj_type != ' ':

            new_tile = tiles.subsurface( (x, y, WIDTH, HEIGHT) )
            #new_tile = Asset(new_tile, x, y)

            if obj_type == 'B':
                new_tile = Background(new_tile, x, y)
            elif obj_type == 'X':
                new_tile = Obstacle(new_tile, x, y)
            elif obj_type == 'O':
                new_tile = Object(new_tile, x, y)
            elif obj_type == 'F':
                new_tile = Foreground(new_tile, x, y)



            square.layers.append(new_tile)

        world_row.append(square)
    world.append(world_row)

# player_sheet = pygame.image.load('town_rpg_pack/graphics/hero.png')


new_tile = tiles.subsurface( (8 * WIDTH, 8 * HEIGHT, WIDTH, HEIGHT) )

player_asset = Asset(new_tile)

WORLD_WIDTH = len(world[0]) * WIDTH * SCALE
WORLD_HEIGHT = len(world) * HEIGHT * SCALE
