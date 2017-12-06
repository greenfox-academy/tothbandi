
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'white')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def draw_field(posx, posy, size, color):
    field = canvas.create_rectangle(posx, posy, posx + size, posy + size, fill = color)

delta = 296//8
ok = True
color = ''
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        draw_field(i * delta + 2, j * delta + 2, delta, color)

root.mainloop()