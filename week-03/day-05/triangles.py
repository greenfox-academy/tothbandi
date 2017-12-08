from tkinter import *
from time import sleep
from random import randrange

root = Tk()

cw=600
ch=600
canvas = Canvas(root, width=cw, height=ch, bg='white')
canvas.pack()

def tri(x, y, width, height):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    color = colors[randrange(len(colors))]
    canvas.create_polygon(  x,              y,
                            x + width,      y,
                            x + width / 2,  y + height,
                            outline = 'black',
                            fill = color
                        )
    sleep(0.01)
    canvas.update()

def tri_triangle(x, y, width, height):
    if width < 18:
        return None
    tri(x, y, width / 2, height / 2)
    tri(x + width / 2, y, width / 2, height / 2)
    tri(x + width / 4, y + height / 2, width / 2, height / 2)
    tri_triangle(x, y, width / 2, height / 2)
    tri_triangle(x + width / 2, y, width / 2, height / 2)
    tri_triangle(x + width / 4, y + height / 2, width / 2, height / 2)

tri_triangle(2, 2, cw - 2, ch - 2)

root.mainloop()