# import tile
# # import boards
# # import view
# # import hero
# import skeleton
# import floor
# import wall
# from random import randint, randrange
from math import pow, sqrt

class Control(object):
    def __init__(self, view, board, hero, monsters):
        self.view = view
        self.board = board
        self.hero = hero
        self.monsters = monsters
        # self.view.init_board(self.board)
        # self.view.init_hero(self.hero)
        # self.skeletons = self.monsters.monsters
        # # self.set_skeletons()
        # self.view.init_skeletons(self.skeletons)
        # self.canvas = self.view.get_canvas()
        self.delay = 1
        self.direction = ['left', 'up', 'right', 'down']
    
# main.canvas.bind("<KeyPress>", main.on_key_press)
# main.canvas.focus_set()

# main.view.root_mainloop()

    def start_game(self):
        self.view.init_board(self.board)
        self.view.init_hero(self.hero)
        self.view.init_skeletons(self.monsters)
        self.view.init_hud(self.hero)
        self.view.canvas.bind("<KeyPress>", self.on_key_press)
        self.view.mainloop()

    def on_key_press(self, e):
        direction = str(e.keysym).lower()
        if  direction in self.direction:
            self.view.redraw_tile(self.board.board[self.hero.posx][self.hero.posy])
            self.view.draw_hud(self.hero)
            self.hero.move(direction, self.can_go(self.hero, direction))
            self.view.draw_hero(self.hero)
            self.on_skeleton(self.hero)
            if self.delay == 2:
                self.move_skeletons()
                self.delay = 0
            self.delay += 1

    def move_skeletons(self):
        for i, skeleton in enumerate(self.monsters.monsters):
            self.view.redraw_tile(self.board.board[skeleton.posx][skeleton.posy])
            self.move_skeleton(skeleton, i)
            self.on_hero(skeleton)
        self.view.draw_skeletons(self.monsters.monsters)

    def move_skeleton(self, skeleton, index):
        sx = skeleton.posx
        sy = skeleton.posy
        hx = self.hero.posx
        hy = self.hero.posy
        dist = sqrt(pow(sx - hx, 2) + pow(sy - hy, 2))
        next_dist = []
        if self.can_go(skeleton, 'left'):
            next_dist.append(sqrt(pow(sx - 1 - hx, 2) + pow(sy - hy, 2)))
        else:
            next_dist.append(1000)
        if self.can_go(skeleton, 'up'):
            next_dist.append(sqrt(pow(sx - hx, 2) + pow(sy - 1 - hy, 2)))
        else:
            next_dist.append(1000)
        if self.can_go(skeleton, 'right'):
            next_dist.append(sqrt(pow(sx + 1 - hx, 2) + pow(sy - hy, 2)))
        else:
            next_dist.append(1000)
        if self.can_go(skeleton, 'down'):
            next_dist.append(sqrt(pow(sx - hx, 2) + pow(sy + 1 - hy, 2)))
        else:
            next_dist.append(1000)
        i = next_dist.index(min(next_dist))
        dir = ['left', 'up', 'right', 'down']
        if next_dist[i] < 1000 and self.not_on_another_skeleton(index, dir[i]):
            skeleton.move(dir[i], True)

    def not_on_another_skeleton(self, index, direction):
        sx = self.monsters.monsters[index].posx
        sy = self.monsters.monsters[index].posy
        if direction == 'left':
            sx -= 1
        if direction == 'up':
             sy -= 1           
        if direction == 'right':
            sx += 1
        if direction == 'down':
            sy += 1
        for i in range(len(self.monsters.monsters)):
            ax = self.monsters.monsters[i].posx
            ay = self.monsters.monsters[i].posy
            if not i == index:
                if sx == ax and sy == ay:
                    return False
        return True

    def on_skeleton(self, charac):
        on_skeleton = None
        for skeleton in self.monsters.monsters:
            if charac.posx == skeleton.posx and charac.posy == skeleton.posy:
                on_skeleton = skeleton
        if not on_skeleton == None:
            self.view.draw_hud(on_skeleton)
            self.monsters.monsters.remove(on_skeleton)
            self.view.init_skeletons(self.monsters)
    
    def on_hero(self, skeleton):
        if self.hero.posx == skeleton.posx and self.hero.posy == skeleton.posy:
            self.view.draw_hud(skeleton)
            self.monsters.monsters.remove(skeleton)
            self.view.init_skeletons(self.monsters)
                
    def character_move(self, charac, direction):
        charac.move(direction, self.can_go(charac, direction))

    def can_go(self, charac, direction):
        if direction == 'left' and charac.posx - 1 >= 0:
            return self.board.board[charac.posx - 1][charac.posy].is_permeable
        elif direction == 'up' and charac.posy - 1 >= 0:
            return self.board.board[charac.posx][charac.posy - 1].is_permeable
        elif direction == 'right' and charac.posx + 1 < len(self.board.board[0]):
            return self.board.board[charac.posx + 1][charac.posy].is_permeable            
        elif direction == 'down' and charac.posy + 1 < len(self.board.board):
            return self.board.board[charac.posx][charac.posy + 1].is_permeable