from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'white')
canvas.pack()

# draw a box that has different colored lines on each edge.

box_top = canvas.create_line(50, 50, 250, 50, fill = 'red', width = 3)
box_top = canvas.create_line(250, 50, 250, 250, fill = 'green', width = 3)
box_top = canvas.create_line(250, 250, 50, 250, fill = 'blue', width = 3)
box_top = canvas.create_line(50, 250, 50, 50, fill = 'orange', width = 3)

root.mainloop()