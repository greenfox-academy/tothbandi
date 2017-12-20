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

    def init_hero(self, hero):
        self.character_images.append(PhotoImage(file = hero.image))
        self.draw_tile(hero, self.character_images[0])

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
 
    def get_canvas(self):
        return self.canvas

    def root_mainloop(self):
        self.root.mainloop()

    #  def on_key_press(e):
    #     if e.keycode == 40: # le
    #         # self.draw_tile(hero.posx, hero.posy, img) kell global hero
    #         pass
    #     elif e.keycode == 39:
    #         pass


    # def do_game(self):

    #     # and lower if the key that was pressed the down arrow
    #     # draw the box again in the new position
    #     box.draw(canvas)

    #     # Tell the canvas that we prepared a function that can deal with the key press events
    #     canvas.bind("<KeyPress>", on_key_press)
    #     canvas.pack()

    #     # Select the canvas to be in focused so it actually recieves the key hittings
    #     canvas.focus_set()

    #     # Draw the box in the initial position
    #     box.draw(canvas)
    


    # def get_tiles_in_row(self):    # boardba
    #     return len(self.board[0])
    
    # def get_tiles_in_col(self):    # boardba
    #     return len(self.board)


    

        