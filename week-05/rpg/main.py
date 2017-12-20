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
        self.view.root_mainloop()
    
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

Main()



