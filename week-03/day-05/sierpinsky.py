from tkinter import *
from time import sleep
from random import randrange

root = Tk()

cw=600
ch=600
canvas = Canvas(root, width=cw, height=ch, bg='white')
canvas.pack()

def draw_sq(x1, y1, x2, y2):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    color = colors[randrange(len(colors))]
    canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill=color)
    sleep(0.00001)
    canvas.update()

def square(x, y, width, height):
    if width < 5:
        return None

    w3 = width / 3
    h3 = height / 3

    draw_sq(x + w3,     y + h3,
            x + 2 * w3, y + 2 * h3)
    
    for i in range(3):
        for j in range(3):
            if not (j == 1 and i == 1):
                square(x + j * w3, y + i * h3, w3, h3)

square(2, 2, cw - 2, ch - 2)

root.mainloop()