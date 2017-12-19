class Character(object):
    def __init__(self, posx, posy, max_health_point, current_health_point, defend_point, strike_point):
        self.posx = posx
        self.posy = posy
        self.max_health_point = max_health_point
        self.current_health_point = current_health_point
        self.defend_point = defend_point
        self.strike_point = strike_point

class Hero(Character):
    image = 'hero-down.png'
    def __init__(self, posx, posy, max_health_point, current_health_point, defend_point, strike_point):
        super().__init__(posx, posy, max_health_point, current_health_point, defend_point, strike_point)

    