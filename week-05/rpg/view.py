from tkinter import *
import boards
import tile
import character

class View(object):
    def __init__(self, board):
        self.board = board.get_board()
        self.root = Tk()
        self.canvas_width = 0
        self.canvas_height = 0
        self.canvas = None
        self.ratio = 0.0
    
    def get_tile_width(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.width()
    
    def get_tile_height(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.height()

    def get_tiles_in_row(self):
        return len(self.board[0])
    
    def get_tiles_in_col(self):
        return len(self.board)
    
    def get_board_width(self):
        tile_width = self.get_tile_width()
        tiles_in_row = self.get_tiles_in_row()
        return tiles_in_row * tile_width

    def get_board_height(self):
        tile_height = self.get_tile_height()
        tiles_in_col = self.get_tiles_in_col()
        return tiles_in_col * tile_height

    def set_ratio(self, screen_width, screen_height, board_width, board_height):
        width_ratio = screen_width / board_width
        if width_ratio > 1.0:
            width_ratio = 1.0
        height_ratio = screen_height / board_height
        if width_ratio > 1.0:
            width_ratio = 1.0
        self.ratio = width_ratio if width_ratio < height_ratio else height_ratio
    
    def get_ratio(self):
        return self.ratio

    def set_canvas_width(self, width):
        self.canvas_width = width
    
    def set_canvas_height(self, height):
        self.canvas_height = height

    def set_canvas_size(self):
        screen_width = self.root.winfo_screenwidth() - 20 # because of fine adjustment
        screen_height = self.root.winfo_screenheight() - 168 # because of Windows taskbar
        board_width = self.get_board_width()
        board_height = self.get_board_height()
        self.set_ratio(screen_width, screen_height, board_width, board_height)
        ratio = self.get_ratio()
        canvas_width = board_width * ratio + 8
        canvas_height = board_height * ratio + 8
        self.set_canvas_width(canvas_width)
        self.set_canvas_height(canvas_height)

    def set_canvas(self):
        self.canvas = Canvas(self.root, width = self.canvas_width, height = self.canvas_height)
        self.canvas.pack()
    
    def get_canvas(self):
        return self.canvas
    
    def draw_board(self):
        row = self.get_tiles_in_row()
        col = self.get_tiles_in_col()
        act_board = self.board
        tiles = []
        global images
        images = []
        ratio = self.get_ratio()
        for i in range(col):
            tiles.append([])
            images.append([])
            for j in range(row):
                if act_board[i][j] == '0':
                    tiles[i].append(tile.Floor(4 + j * 72, 4 + i * 72))
                    images[i].append(PhotoImage(file = tiles[i][j].image))
                else:
                    tiles[i].append(tile.Wall(4 + j * 72, 4 + i * 72))
                    images[i].append(PhotoImage(file = tiles[i][j].image))
                image_id = self.canvas.create_image(tiles[i][j].posx, tiles[i][j].posy, anchor = 'nw', image = images[i][j])
                self.canvas.scale(image_id, 0, 0, ratio, ratio)
    
    def draw_hero(self, hero):
        global img
        img = PhotoImage(file = hero.image)
        img_id = self.canvas.create_image(0,0, anchor = 'nw', image = img)
        self.canvas.scale(img_id, 0, 0, self.get_ratio(), self.get_ratio())

    def root_mainloop(self):
        self.root.mainloop()
    

        