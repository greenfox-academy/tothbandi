
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'white')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def line_to_center(from_x, from_y):
    line = canvas.create_line(from_x, from_y, 150, 150, fill = 'red', width = 3)

line_to_center(10, 270)
line_to_center(120, 290)
line_to_center(270, 30)

root.mainloop()