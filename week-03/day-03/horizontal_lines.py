from tkinter import *
from random import randrange

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def line50(from_x, from_y):
    way = 1
    if randrange(0, 2) == 0:
        way = -1
    print(way)
    if from_x + 50 * way < 0 or from_x + 50 * way > 300:
        way *= -1
    line = canvas.create_line(from_x, from_y, from_x + 50 * way, from_y, fill='red', width = 3)

line50(10, 20)
line50(80, 80)
line50(270, 190)

root.mainloop()