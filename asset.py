import pygame

WIDTH = 16
HEIGHT = 16

SCALE = 2

class Asset():

    def __init__(self, image, x = 0, y = 0):

        self.x = x * SCALE
        self.y = y * SCALE
        self.width = WIDTH * SCALE
        self.height = HEIGHT * SCALE
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y, self.width, self.height))
