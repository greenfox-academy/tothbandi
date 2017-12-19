from tkinter import *
import boards
import tile
import character

class View(object):
    def __init__(self, board):
        self.board = board # .get_board()
        self.root = Tk()
        self.canvas_width = 0
        self.canvas_height = 0
        self.canvas = None
        self.ratio = 0.0
        self.images = []
        self.tiles = []
        self.init_board()
    
    def init_board(self):
        self.set_canvas_size()
        self.set_canvas()
        self.create_board()
        self.init_hero()
        # self.do_game()
        self.root_mainloop()
    
    def on_key_press(e):
        if e.keycode == 40: # le
            # self.draw_tile(hero.posx, hero.posy, img) kell global hero
            pass
        elif e.keycode == 39:
            pass


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
    

    def get_tile_width(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.width()
    
    def get_tile_height(self):
        atile = tile.Floor(0,0)
        img = PhotoImage(file = atile.image)
        return img.height()

    # def get_tiles_in_row(self):    # boardba
    #     return len(self.board[0])
    
    # def get_tiles_in_col(self):    # boardba
    #     return len(self.board)
    
    def get_board_width(self):
        tile_width = self.get_tile_width()
        tiles_in_row = self.board.get_row()
        return tiles_in_row * tile_width

    def get_board_height(self):
        tile_height = self.get_tile_height()
        tiles_in_col = self.board.get_col()
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
    
    def draw_tile(self, posx, posy, img):
        img_id = self.canvas.create_image(posx, posy, anchor = 'nw', image = img)
        self.canvas.scale(img_id, 0, 0, self.get_ratio(), self.get_ratio())

    def create_board(self):
        row = self.board.get_row()
        col = self.board.get_col()
        act_board = self.board.get_board()
        tiles = self.tiles
        images = self.images
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
                self.draw_tile(tiles[i][j].posx, tiles[i][j].posy,images[i][j])
    
    def init_hero(self):
        hero = character.Hero(0, 0, 11, 11, 11, 11)
        global img
        img = PhotoImage(file = hero.image)
        self.draw_tile(hero.posx, hero.posy, img)

    def root_mainloop(self):
        self.root.mainloop()
    

        