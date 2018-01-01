from tile import Tile

class Character(Tile):
    def __init__(self, image, posx, posy, max_health_point, current_health_point, defend_point, strike_point):
        super().__init__(image, posx, posy)
        self.max_health_point = max_health_point
        self.current_health_point = current_health_point
        self.defend_point = defend_point
        self.strike_point = strike_point
        # self.direction = {37: 'left', 38: 'up', 39: 'right', 40: 'down'}

    def move(self, direction):
        if direction == 'left':
            self.posx -= 1
        elif direction == 'up':
            self.posy -= 1
        elif direction == 'right':
            self.posx += 1
        elif direction == 'down':
            self.posy += 1
