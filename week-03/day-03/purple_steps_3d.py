from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bg = 'white')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def rect(pos, size):
    square = canvas.create_rectangle(pos, pos, pos + size, pos + size , fill = 'purple')

delta = 10
j=0
for i in range(5):
    j += i
    rect(j*delta, (i+1)*delta)

root.mainloop()