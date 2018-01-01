from tkinter import *
import boards
# import tile
# import character
# import hero

class View(object):
    def __init__(self):
        self.root = Tk()

        self.board = []
        self.tile_width = 0
        self.tile_height = 0
        self.canvas_width = 0
        self.canvas_height = 0
        self.canvas = None
        self.board_images = []
        self.hero_image = None
        self.skeleton_images = []
        self.character_images = []
        self.offsetX = 4
        self.offsetY = 4
        self.hud_canvas = None
        self.hud = None

    def init_board(self, board):
        self.board = board.board
        self.set_canvas_size()
        self.set_canvas()
        self.draw_board()

    def set_canvas_size(self):
        board_width = self.get_board_width()
        board_height = self.get_board_height()
        self.canvas_width = board_width + self.offsetX
        self.canvas_height = board_height + self.offsetY
    
    def get_board_width(self):
        self.set_tile_width()
        tiles_in_row = len(self.board[0])
        return tiles_in_row * self.tile_width

    def get_board_height(self):
        self.set_tile_height()
        tiles_in_col = len(self.board)
        return tiles_in_col * self.tile_height

    def set_tile_width(self):
        tile = self.board[0][0]
        img = PhotoImage(file = tile.image)
        self.tile_width = img.width()

    def set_tile_height(self):
        tile = self.board[0][0]
        img = PhotoImage(file = tile.image)
        self.tile_height = img.height()

    def set_canvas(self):
        self.root.title('Wanderer Game Exercise')
        self.canvas = Canvas(self.root, width = self.canvas_width, height = self.canvas_height)
        self.canvas.pack()
        self.canvas.focus_set()
    
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

    def init_hero(self, hero):
        self.hero_image = PhotoImage(file = hero.image)
        self.draw_tile(hero, self.hero_image)
        # self.init_hud(hero)
    
    def init_skeletons(self, monsters):
        self.skeleton_images = []
        for skeleton in monsters.monsters:
            self.skeleton_images.append(PhotoImage(file = skeleton.image))
            self.draw_tile(skeleton, self.skeleton_images[-1])

    def init_hud(self, charac):
        self.hud = Text(self.root, height = 2, width = 60)
        # self.hud.pack()
        self.hud.pack(side='top')
        self.hud.config(state = 'disabled')
        self.draw_hud(charac)

    def draw_hud(self, charac):
        text = self.hud.get('1.0', 'end-1c')
        # if isinstance(charac, 'hero.Hero'):
        if type(charac).__name__ == 'Hero':
            text = 'Hero:     (Level {}) HP: {}/{} | DP: {} | SP: {}'
            level = self.get_level()
        else:
            text += '\nSkeleton: (Level {}) HP: {}/{} | DP: {} | SP: {}'
            level = charac.level
        hp = charac.current_health_point
        max_hp = charac.max_health_point
        dp = charac.defend_point
        sp = charac.strike_point
        text = text.format(level, hp, max_hp, dp, sp)
        self.hud.config(state = 'normal')
        self.hud.delete('1.0', 'end')
        self.hud.insert('end', text)
        self.hud.config(state = 'disabled')

        
    def init_character(self, charac):
        self.character_images.append(PhotoImage(file = charac.image))
        self.draw_tile(charac, self.character_images[-1])
        if len(self.character_images) == 1:
            self.init_hud(charac)
    

       

    
    def get_text(self, charac):
        pass

    def get_level(self):
        board = boards.Boards()
        return board.level










    
    def redraw_tile(self, tile):
        self.draw_tile(tile, self.board_images[tile.posx][tile.posy])

    def draw_hero(self, hero):
        self.hero_image = PhotoImage(file = hero.image)
        self.draw_tile(hero, self.hero_image)

    def draw_skeletons(self, skeletons):
        for index, skeleton in enumerate(skeletons):
            self.draw_tile(skeleton, self.skeleton_images[index])

    def get_canvas(self):
        return self.canvas

    def mainloop(self):
        self.root.mainloop()
