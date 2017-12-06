from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bg = 'white', bd= 10)
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def rect(pos, size):
    square = canvas.create_rectangle(pos, pos, pos + size, pos + size , fill = 'purple')

delta = 10

for i in range(20):
    rect(i*delta, delta)


root.mainloop()