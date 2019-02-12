#!/usr/bin/python3

import pygame

from init import world, WORLD_WIDTH, WORLD_HEIGHT, player_asset



pygame.init()

size = width, height = (WORLD_WIDTH, WORLD_HEIGHT)

screen = pygame.display.set_mode(size)

player_x = 16
player_y = 10


running = True

pygame.time.set_timer(pygame.USEREVENT, 500)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            player_y += 1

        player_asset.x = 32 * player_x
        player_asset.y = 32 * player_y


        for world_row in world:
            for square in world_row:
                for asset in square.layers:

                    # POLYMORPHISM
                    # calling a method without knowing which subclass this is an instance of
                    asset.draw(screen)


                    # NOT POLYMORPHISM
                    # determining which function to call specifically based on object type
                    # if isinstance(asset, Foreground):
                    #     foreground_draw(asset)
                    # elif isinstance(asset, Background):
                    #     background_draw(asset)
                    # elif isinstance(asset, Obstacle):
                    #     obsctacle_draw(asset)
                    # elif isinstance(asset, Object):
                    #     object_draw(asset)
                    # ... etc. ...
        player_asset.draw(screen)
        pygame.display.flip()


