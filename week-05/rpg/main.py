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
        self.view.init_character(self.hero)
        self.canvas = self.view.get_canvas()
        self.skeletons = []
        self.set_skeletons()
        self.init_skeletons()
    
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
        max_skeletons = 3
        max_x = self.act_board.get_max_col()
        max_y = self.act_board.get_max_row()
        i = 0
        while i < max_skeletons:
            posx = randrange(max_x)
            posy = randrange(max_y)
            if self.free_position(posx, posy):
                i += 1
                self.skeletons.append(character.Skeleton(posx, posy))
    
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
        if e.keycode == 37: # bal
            self.hero_left()
        elif e.keycode == 38: # fel
            self.hero_up()
        elif e.keycode == 39: # jobb
            self.hero_right()
        elif e.keycode == 40: # le
            self.hero_down()
        self.view.draw_hero(self.hero)
    
    def hero_left(self):
        self.hero.move_left(self.can_go(self.hero, 'left'))

    def hero_up(self):
        self.hero.move_up(self.can_go(self.hero, 'up'))

    def hero_right(self):
        self.hero.move_right(self.can_go(self.hero, 'right'))

    def hero_down(self):
        self.hero.move_down(self.can_go(self.hero, 'down'))

    def can_go(self, character, direction):
        if direction == 'left' and character.posx - 1 >= 0:
            return self.board[character.posx - 1][character.posy].is_permeable
        elif direction == 'up' and character.posy - 1 >= 0:
            return self.board[character.posx][character.posy - 1].is_permeable
        elif direction == 'right' and character.posx + 1 < len(self.board[0]):
            return self.board[character.posx + 1][character.posy].is_permeable            
        elif direction == 'down' and character.posy + 1 < len(self.board):
            return self.board[character.posx][character.posy + 1].is_permeable

main = Main()

main.canvas.bind("<KeyPress>", main.on_key_press)
main.canvas.focus_set()

main.view.root_mainloop()



