from tkinter import *
from time import sleep
from random import randrange
from math import sin, cos, radians

root = Tk()

cw=600
ch=600
canvas = Canvas(root, width=cw, height=ch, bg='deep sky blue')
canvas.pack()

def line(x, y, angle, length):
    d_ang = radians(25)
    ratio = 0.95

    if length < 40:
        return None

    x1 = x + sin(angle)*length 
    y1 = y - cos(angle)*length 
    canvas.create_line(x, y, x1, y1, fill='saddle brown')

    line(x1, y1, angle + d_ang, length * ratio)
    line(x1, y1, angle - d_ang, length * ratio)
    line(x1, y1, angle, length * ratio)

line(cw/2, ch - ch/10, 0, ch/10)


root.mainloop()