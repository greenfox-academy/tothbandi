from tkinter import *
import tile
import boards
import view

board = boards.Boards()


view = view.View(board)
view.set_canvas_size()

view.set_canvas()

view.draw_board()
