from tkinter import *
import tile
import boards
import view
import character
from random import randint, randrange

class Main(object):
    def __init__(self):
        self.act_board = boards.Boards()
        self.board = []
        self.set_board(self.act_board)
        self.hero = character.Hero()
        self.view = view.View()
        self.view.init_board(self.board)
        self.init_character(self.hero)
        self.canvas = self.view.get_canvas()
        self.skeletons = []
        self.set_skeletons()
    
    def init_character(self, charac):
        if type(charac) == character.Hero:
            mhp = 20 + 3 * 6
            hp = 20 + 3 * self.d6()
            dp = 2 * self.d6()
            sp = 5 + self.d6()
        else:
            level = self.randlevel()
            mhp = 2 * level * 6
            hp = 2 * level * self.d6()
            dp = int(level / 2 * self.d6())
            sp = level * self.d6()
            if charac.is_boss:
                mhp += 6
                hp += self.d6()
                dp += int(self.d6() / 2)
                sp += level
            charac.level = level
        charac.max_health_point = mhp
        charac.current_health_point = hp
        charac.defend_point = dp
        charac.strike_point = sp
        self.view.init_character(charac)

    def d6(self):
        return randint(1, 6)

    def randlevel(self):
        level = self.act_board.level
        rand = randrange(100)
        if rand < 50:
            pass
        elif rand < 90:
            level += 1
        else:
            level += 2
        return level

    def set_board(self, act_board):
        row = act_board.get_max_row()
        col = act_board.get_max_col()
        pattern = act_board.get_board()
        for i in range(row):
            self.board.append([])
            for j in range(col):
                if pattern[i][j] == '0':
                    self.board[i].append(tile.Floor(i, j))
                else:
                    self.board[i].append(tile.Wall(i, j))
    
    def set_skeletons(self):
        max_skeletons = randint(3, 6)
        max_x = self.act_board.get_max_col()
        max_y = self.act_board.get_max_row()
        i = 0
        while i < max_skeletons:
            posx = randrange(max_x)
            posy = randrange(max_y)
            if self.free_position(posx, posy):
                self.skeletons.append(character.Skeleton(posx, posy))
                i += 1
        self.set_boss()
        self.set_key_keeper()
        for skeleton in self.skeletons:
            self.init_character(skeleton)
    
    def set_boss(self):
        boss = randrange(len(self.skeletons))
        self.skeletons[boss].set_to_boss()
    
    def set_key_keeper(self):
        key = randrange(len(self.skeletons))
        while not self.skeletons[key].has_key:
            key = randrange(len(self.skeletons))
            self.skeletons[key].set_key()

    def init_skeletons(self):
        for skeleton in self.skeletons:
            self.view.init_character(skeleton)

    def free_position(self, posx, posy):
        return self.not_hero(posx, posy) and self.not_wall(posx, posy) and self.not_skeleton(posx, posy)

    def not_hero(self, posx, posy):
        return not (posx == self.hero.posx and posy == self.hero.posy)

    def not_wall(self, posx, posy):
        return self.board[posx][posy].is_permeable
    
    def not_skeleton(self, posx, posy):
        for i in range(len(self.skeletons)):
            if posx == self.skeletons[i].posx and posy == self.skeletons[i].posy:
                return False
        return True

    def on_key_press(self, e):
        self.view.redraw_tile(self.board[self.hero.posx][self.hero.posy])
        self.view.draw_hud(self.hero)
        direction = ''
        if e.keycode == 37:
            direction = 'left'
        elif e.keycode == 38:
            direction = 'up'
        elif e.keycode == 39:
            direction = 'right'
        elif e.keycode == 40:
            direction = 'down'
        self.hero.move(direction, self.can_go(self.hero, direction))
        self.view.draw_hero(self.hero)
        self.on_skeleton(self.hero)

    def on_skeleton(self, charac):
        for skeleton in self.skeletons:
            if charac.posx == skeleton.posx and charac.posy == skeleton.posy:
                self.view.draw_hud(skeleton)
    
    def character_move(self, charac, direction):
        charac.move(direction, self.can_go(charac, direction))

    def can_go(self, charac, direction):
        if direction == 'left' and charac.posx - 1 >= 0:
            return self.board[charac.posx - 1][charac.posy].is_permeable
        elif direction == 'up' and charac.posy - 1 >= 0:
            return self.board[charac.posx][charac.posy - 1].is_permeable
        elif direction == 'right' and charac.posx + 1 < len(self.board[0]):
            return self.board[charac.posx + 1][charac.posy].is_permeable            
        elif direction == 'down' and charac.posy + 1 < len(self.board):
            return self.board[charac.posx][charac.posy + 1].is_permeable

main = Main()

main.canvas.bind("<KeyPress>", main.on_key_press)
main.canvas.focus_set()

main.view.root_mainloop()



