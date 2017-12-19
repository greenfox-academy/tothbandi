from tkinter import *
import boards
import tile

class View(object):
    def __init__(self, board):
        self.board = board.get_board()
        self.root = Tk()
        self.canvas_width = 0
        self.canvas_height = 0
    
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

    def get_ratio(self, screen_width, screen_height, board_width, board_height):
        width_ratio = screen_width / board_width
        if width_ratio > 1.0:
            width_ratio = 1.0
        height_ratio = screen_height / board_height
        if width_ratio > 1.0:
            width_ratio = 1.0
        ratio = width_ratio if width_ratio < height_ratio else height_ratio
        return ratio

    def set_canvas_width(self, width):
        self.width = width
    
    def set_canvas_height(self, height):
        self.height = height

    def set_canvas_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight() - 168 # because of Windows taskbar
        board_width = self.get_board_width()
        board_height = self.get_board_height()
        ratio = self.get_ratio(screen_width, screen_height, board_width, board_height)
        canvas_width = board_width * ratio + 4
        canvas_height = board_height * ratio + 4
        self.set_canvas_width(canvas_width)
        self.set_canvas_height(canvas_height)

        print('set_canvas_size')
        print(str(board_width) + ' ' + str(board_height))
        print(str(canvas_width) + ' ' + str(canvas_height))
        