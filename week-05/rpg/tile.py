class Tile(object):
    def __init__(self, image, posx, posy, is_permeable):
        self.image = image
        self.posx = posx
        self.posy = posy
        self.is_permeable = is_permeable

class Floor(Tile):
    image = 'floor.png'
    is_permeable = True
    def __init__(self, posx, posy):
        super().__init__(Floor.image, posx, posy, Floor.is_permeable)

class Wall(Tile):
    image = 'wall.png'
    is_permeable = False
    def __init__(self, posx, posy):
        super().__init__(Wall.image, posx, posy, Wall.is_permeable)