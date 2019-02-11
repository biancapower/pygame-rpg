#!/usr/bin/python3

import pygame

from init import world, WORLD_WIDTH, WORLD_HEIGHT



pygame.init()

size = width, height = (WORLD_WIDTH, WORLD_HEIGHT)

screen = pygame.display.set_mode(size)


running = True

pygame.time.set_timer(pygame.USEREVENT, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        for world_row in world:
            for square in world_row:
                for graphic in square.graphics:
                    graphic.draw(screen)

        pygame.display.flip()


