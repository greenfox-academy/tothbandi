from character import Character
from randomize import Randomize
from boards import Boards

class Skeleton(Character):

    one_is_boss = False

    def __init__(self, posx, posy):
        self.image = 'accessories/skeleton.png'    
        self.is_boss = False
        self.has_key = False
        self.rand = Randomize()
        self.level = self.rand.randlevel(Boards().level)
        self.max_health_point = self.set_max_health_point()
        self.current_health_point = self.set_current_health_point()
        self.defend_point = self.set_defend_point()
        self.strike_point = self.set_strike_point()        
        super().__init__(self.image, posx, posy, self.max_health_point, self.current_health_point, self.defend_point, self.strike_point)
    
    def set_to_boss(self):
        if not Skeleton.one_is_boss:
            Skeleton.one_is_boss = True
            self.is_boss = True
            self.image = 'accessories/boss.png'
            self.max_health_point += 6
            self.current_health_point += self.rand.d6()
            self.defend_point += int(self.rand.d6() / 2)
            self.strike_point += self.level
    
    def set_key(self):
        if not self.is_boss:
            self.has_key = True

    def move(self, direction, can_go):
        if can_go:
            super().move(direction)
    
    def set_max_health_point(self):
        return 2 * self.level * 6
    
    def set_current_health_point(self):
        return 2 * self.level * self.rand.d6()

    def set_defend_point(self):
        return int(self.level / 2 * self.rand.d6())

    def set_strike_point(self):
        return self.level * self.rand.d6()
