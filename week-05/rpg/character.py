class Character(object):
    def __init__(self, posx, posy, max_health_point, current_health_point, defend_point, strike_point):
        self.posx = posx
        self.posy = posy
        self.max_health_point = max_health_point
        self.current_health_point = current_health_point
        self.defend_point = defend_point
        self.strike_point = strike_point
        
    def move_left(self):
        self.posx -= 1

    def move_up(self):
        self.posy -= 1

    def move_right(self):
        self.posx += 1
        
    def move_down(self):
        self.posy += 1

class Hero(Character):
    def __init__(self, posx = 0, posy = 0, max_health_point = 0, current_health_point = 0, defend_point = 0, strike_point = 0):
        super().__init__(posx, posy, max_health_point, current_health_point, defend_point, strike_point)
        self.image = 'hero-down.png'
    
    def move_left(self, can_go):
        self.image = 'hero-left.png'
        if can_go:
            super().move_left()

    def move_up(self, can_go):
        self.image = 'hero-up.png'
        if can_go:
            super().move_up()

    def move_right(self, can_go):
        self.image = 'hero-right.png'
        if can_go:
            super().move_right()

    def move_down(self, can_go):
        self.image = 'hero-down.png'
        if can_go:
            super().move_down()

class Skeleton(Character):
    def __init__(self, posx = 0, posy = 0, max_health_point = 0, current_health_point = 0, defend_point = 0, strike_point = 0):
        super().__init__(posx, posy, max_health_point, current_health_point, defend_point, strike_point)
        self.image = 'skeleton.png'    
    