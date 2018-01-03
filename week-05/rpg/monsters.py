from skeleton import Skeleton
from random import randint, randrange

class Monsters(object):
    def __init__(self, board, hero):
        self.board = board
        self.hero = hero
        self.monsters = []
        self.set_monsters()
    
    def set_monsters(self):
        max_monsters = randint(3, 6)
        max_x = self.board.get_max_col()
        max_y = self.board.get_max_row()
        i = 0
        while i < max_monsters:
            posx = randrange(max_x)
            posy = randrange(max_y)
            if self.free_position(posx, posy):
                self.monsters.append(Skeleton(posx, posy))
                i += 1
        self.set_boss()
        self.set_key_keeper()
    
    def set_boss(self):
        boss = randrange(len(self.monsters))
        self.monsters[boss].set_to_boss()
    
    def set_key_keeper(self):
        key = randrange(len(self.monsters))
        while not self.monsters[key].has_key:
            key = randrange(len(self.monsters))
            self.monsters[key].set_key()

    def free_position(self, posx, posy):
        return self.not_hero(posx, posy) and self.not_wall(posx, posy) and self.not_skeleton(posx, posy)

    def not_hero(self, posx, posy):
        return not (posx == self.hero.posx and posy == self.hero.posy)

    def not_wall(self, posx, posy):
        return self.board.board[posx][posy].is_permeable
    
    def not_skeleton(self, posx, posy):
        for i in range(len(self.monsters)):
            if posx == self.monsters[i].posx and posy == self.monsters[i].posy:
                return False
        return True