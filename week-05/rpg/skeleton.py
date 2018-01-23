from character import Character
from randomize import Randomize
from boards import Boards

class Skeleton(Character):

    one_is_boss = False

    def __init__(self, posx, posy, level = Randomize().randlevel(Boards().level)):
        self.level = level
        super().__init__(
            'accessories/skeleton.png',
            posx,
            posy,
            self.set_max_health_point(),
            self.set_current_health_point(),
            self.set_defend_point(),
            self.set_strike_point()
            )
        self.is_boss = False
        self.has_key = False
    
    def set_to_boss(self):
        if not Skeleton.one_is_boss:
            Skeleton.one_is_boss = True
            self.is_boss = True
            self.image = 'accessories/boss.png'
            self.max_health_point += 6
            self.current_health_point += Randomize().d6()
            self.defend_point += int(Randomize().d6() / 2)
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
        return 2 * self.level * Randomize().d6()

    def set_defend_point(self):
        return int(self.level / 2 * Randomize().d6())

    def set_strike_point(self):
        return self.level * Randomize().d6()
