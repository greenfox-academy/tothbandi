from tile import Tile

class Wall(Tile):
    image = 'accessories/wall.png'
    is_permeable = False
    def __init__(self, posx, posy):
        super().__init__(Wall.image, posx, posy)
