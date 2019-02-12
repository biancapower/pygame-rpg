from tile import *

class Object(Tile):

    def is_passable(self):
        return False