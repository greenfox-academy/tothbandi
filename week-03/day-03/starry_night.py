from tkinter import *
from secrets import token_hex
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def star():
    posx=randint(0,300)
    posy=randint(0,300)
    size=randint(5,9)
    any_grey='#' + token_hex(1)*3
    square = canvas.create_rectangle(posx, posy, posx+size, posy+size, fill = any_grey)

for _ in range(100):
    star()

root.mainloop()