from tkinter import *
import tile
import boards
import view
import character

class Main(object):
    def __init__(self):
        self.act_board = boards.Boards()
        self.board = []
        self.set_board(self.act_board)
        self.hero = character.Hero()
        self.view = view.View()
        self.view.init_board(self.board)
        self.view.init_hero(self.hero)
        self.canvas = self.view.get_canvas()
    
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

    def on_key_press(self, e):
        if e.keycode == 37: # bal
            self.hero_left()
        elif e.keycode == 38: # fel
            self.hero_up()
        elif e.keycode == 39: # jobb
            self.hero_right()
        elif e.keycode == 40: # le
            self.hero_down()
    
    def hero_left(self):
        self.view.redraw_tile(self.board[self.hero.posx][self.hero.posy])
        self.hero.move_left(True)
        self.view.draw_hero(self.hero)

    def hero_up(self):
        self.view.redraw_tile(self.board[self.hero.posx][self.hero.posy])
        self.hero.move_up(True)
        self.view.draw_hero(self.hero)

    def hero_right(self):
        self.view.redraw_tile(self.board[self.hero.posx][self.hero.posy])
        self.hero.move_right(True)
        self.view.draw_hero(self.hero)

    def hero_down(self):
        self.view.redraw_tile(self.board[self.hero.posx][self.hero.posy])
        self.hero.move_down(True)
        self.view.draw_hero(self.hero)

main = Main()

main.canvas.bind("<KeyPress>", main.on_key_press)
main.canvas.focus_set()

main.view.root_mainloop()



