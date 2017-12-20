from tkinter import *
import boards
import tile
import character

class View(object):
    def __init__(self):
        self.board = []
        self.root = Tk()
        self.tile_width = 0
        self.tile_height = 0
        self.canvas_width = 0
        self.canvas_height = 0
        self.canvas = None
        self.board_images = []
        self.character_images = []
        self.offsetX = 2
        self.offsetY = 2

    def init_board(self, board):
        self.board = board
        self.set_canvas_size()
        self.set_canvas()
        self.draw_board()

    def init_character(self, character):
        self.character_images.append(PhotoImage(file = character.image))
        self.draw_tile(character, self.character_images[-1])
        if len(self.character_images) == 1:
            self.init_hud(character)
        
    def init_hud(self, character):
        self.draw_hud(character)
    
    def draw_hud(self, character):
        text = 'Hero (Level {}) HP: {}/{} | DP: {} | SP: {}'
        hp = character.current_health_point
        max_hp = character.max_health_point
        dp = character.defend_point
        sp = character.strike_point
        text = text.format(self.get_level(), hp, max_hp, dp, sp)
        self.canvas.create_text(self.offsetX, self.canvas_height, anchor = 'sw', text = text)
    
    def get_level(self):
        board = boards.Boards()
        return board.level

    def set_canvas_size(self):
        board_width = self.get_board_width()
        board_height = self.get_board_height()
        self.canvas_width = board_width + self.offsetX * 2
        self.canvas_height = board_height + self.offsetY * 2
    
    def get_board_width(self):
        self.set_tile_width()
        tiles_in_row = len(self.board[0])
        return tiles_in_row * self.tile_width

    def get_board_height(self):
        self.set_tile_height()
        tiles_in_col = len(self.board)
        return tiles_in_col * self.tile_height

    def set_tile_width(self):
        atile = self.board[0][0]
        img = PhotoImage(file = atile.image)
        self.tile_width = img.width()

    def set_tile_height(self):
        atile = self.board[0][0]
        img = PhotoImage(file = atile.image)
        self.tile_height = img.height()

    def set_canvas(self):
        self.canvas = Canvas(self.root, width = self.canvas_width, height = self.canvas_height)
        self.canvas.pack()

    def draw_board(self):
        row = len(self.board)
        col = len(self.board[0])
        for i in range(row):
            self.board_images.append([])
            for j in range(row):
                self.board_images[i].append(PhotoImage(file = self.board[i][j].image))
                self.draw_tile(self.board[i][j], self.board_images[i][j])

    def draw_tile(self, tile, image):
        posx = self.offsetX + tile.posx * self.tile_width
        posy = self.offsetY + tile.posy * self.tile_height
        self.canvas.create_image(posx, posy, anchor = 'nw', image = image)
    
    def redraw_tile(self, tile):
        self.draw_tile(tile, self.board_images[tile.posx][tile.posy])

    def draw_hero(self, hero):
        self.character_images[0] = PhotoImage(file = hero.image)
        self.draw_tile(hero, self.character_images[0])
 
    def get_canvas(self):
        return self.canvas

    def root_mainloop(self):
        self.root.mainloop()


    

        