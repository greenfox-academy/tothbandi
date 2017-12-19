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

view.draw_hero()

view.root_mainloop()

