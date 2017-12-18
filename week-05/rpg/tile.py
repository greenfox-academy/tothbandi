class Tile(object):
    def __init__(self, image, posx, posy, is_permeable):
        self.image = image
        self.posx = posx
        self.posy = posy
        self.is_permeable = is_permeable

class Floor(Tile):
    def __init__(self, image, posx, posy):
        self.is_permeable = True
        super().__init__(image, posx, posy, self.is_permeable)
