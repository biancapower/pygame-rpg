from tile import *

class Obstacle(Tile):

    def is_passable(self):
        return False