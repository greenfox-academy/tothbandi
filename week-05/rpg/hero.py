from character import Character
from randomize import Randomize

class Hero(Character):
    def __init__(self, posx = 0, posy = 0):
        self.image = 'accessories/hero-down.png'
        self.direction = {37: 'left', 38: 'up', 39: 'right', 40: 'down'}
        self.rand = Randomize()
        self.max_health_point = 20 + 3 * 6
        self.current_health_point = self.set_current_health_point()
        self.defend_point = self.set_defend_point()
        self.strike_point = self.set_strike_point()
        super().__init__(self.image, posx, posy, self.max_health_point, self.current_health_point, self.defend_point, self.strike_point)

    
    def move(self, direction, can_go):
        self.image = 'accessories/hero-{}.png'.format(direction)
        if can_go:
            super().move(direction)
    
    def set_max_health_point(self):
        return 20 + 3 * 6
    
    def set_current_health_point(self):
        return 20 + 3 * self.rand.d6()

    def set_defend_point(self):
        return 2 * self.rand.d6()

    def set_strike_point(self):
        return 5 + self.rand.d6()