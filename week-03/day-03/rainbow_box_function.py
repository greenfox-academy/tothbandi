from tkinter import *
from random import randrange
from time import sleep
root = Tk()

canvas = Canvas(root, width=300, height=300, bg = 'white')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def sq(size, color):
    pos = randrange(300)
    sq = canvas.create_rectangle(pos-size//2, pos-size//2, pos+size//2, pos+size//2, fill=color)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

for _ in range(100):
    sq(randrange(300), rainbow[randrange(7)])
    # sleep(0.1) - this line doesn't work, only takes 0.1s * 100 and after draws?
root.mainloop()