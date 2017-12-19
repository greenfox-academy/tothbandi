from tkinter import *
import tile
import boards
import view
import character

board = boards.Boards()

view = view.View(board)
view.set_canvas_size()
view.set_canvas()
view.create_board()

hero = character.Hero(11, 11, 11, 11)
view.draw_hero(hero)

view.root_mainloop()

