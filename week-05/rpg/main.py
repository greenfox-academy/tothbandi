# import tile
# import boards
# import hero
# import skeleton
# import floor
# import wall
from view import View
from boards import Boards
from hero import Hero
from monsters import Monsters
from control import Control

view = View()
board = Boards()
hero = Hero()
monsters = Monsters(board, hero)
game = Control(view, board, hero, monsters)
game.start_game()
