from tkinter import *
import boards
import tile

class View(object):
    def __init__(self, board):
        self.board = board.get_board()
        self.root = Tk()
    
    def get_tile_width(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.width()
    
    def get_tile_height(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.height()    
    
    def get_board_width(self):
        tile_width = self.get_tile_width()
        tiles_in_row = len(self.board[0])
        return tiles_in_row * tile_width

    def get_board_height(self):
        tile_height = self.get_tile_height()
        tiles_in_col = len(self.board)
        return tiles_in_col * tile_height

    def set_canvas_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight() - 168 # because of Windows taskbar
        board_width = self.get_board_width()
        board_height = self.get_board_height()
        print('set_canvas_size')
        print(str(board_width) + ' ' + str(board_height))