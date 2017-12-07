from tkinter import *
from math import sqrt

root = Tk()

c_width = 600
c_height = 600
canvas = Canvas(root, width=c_width, height=c_height, bg='yellow')
canvas.pack()

def draw_hex(x, y, wid):
    he = wid // 2 # length of the hexagon edge
    hh = int(he * sqrt(3)/2) # half of the hexagon height
    if he < 10:
        return
    else:
        hexa = canvas.create_polygon(
            x, y,
            x + he // 2, y - hh,
            x + he + he // 2, y - hh,
            x + 2 * he, y,
            x + he + he // 2, y + hh,
            x + he // 2, y + hh,
            fill="white",
            outline='black'
        )
        draw_hex(x + he // 4, y - hh // 2, wid // 2)
        draw_hex(x + he // 4, y + hh // 2, wid // 2)
        draw_hex(x + he, y, wid//2)


draw_hex(0,c_height//2, c_width)

root.mainloop()