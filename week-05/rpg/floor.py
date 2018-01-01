from tile import Tile

class Floor(Tile):
    image = 'accessories/floor.png'
    is_permeable = True
    def __init__(self, posx, posy):
        super().__init__(Floor.image, posx, posy)
