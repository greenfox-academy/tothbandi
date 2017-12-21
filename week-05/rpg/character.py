class Character(object):
    def __init__(self, posx, posy, max_health_point, current_health_point, defend_point, strike_point):
        self.posx = posx
        self.posy = posy
        self.max_health_point = max_health_point
        self.current_health_point = current_health_point
        self.defend_point = defend_point
        self.strike_point = strike_point

    def move(self, direction):
        if direction == 'left':
            self.posx -= 1
        elif direction == 'up':
            self.posy -= 1
        elif direction == 'right':
            self.posx += 1
        elif direction == 'down':
            self.posy += 1

class Hero(Character):
    def __init__(self, posx = 0, posy = 0, max_health_point = 0, current_health_point = 0, defend_point = 0, strike_point = 0):
        super().__init__(posx, posy, max_health_point, current_health_point, defend_point, strike_point)
        self.image = 'hero-down.png'
    
    def move(self, direction, can_go):
        self.image = 'hero-{}.png'.format(direction)
        if can_go:
            super().move(direction)    
    
class Skeleton(Character):

    one_is_boss = False

    def __init__(self, posx = 0, posy = 0, max_health_point = 0, current_health_point = 0, defend_point = 0, strike_point = 0):
        super().__init__(posx, posy, max_health_point, current_health_point, defend_point, strike_point)
        self.image = 'skeleton.png'    
        self.is_boss = False
        self.has_key = False
    
    def set_to_boss(self):
        if not Skeleton.one_is_boss:
            Skeleton.one_is_boss = True
            self.is_boss = True
            self.image = 'boss.png'
    
    def set_key(self):
        if not self.is_boss:
            self.has_key = True

    def move(self, direction, can_go):
        if can_go:
            super().move(direction)