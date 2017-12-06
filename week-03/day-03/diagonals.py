from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'white')
canvas.pack()

# draw the canvas' diagonals in green.

di1 = canvas.create_line(0, 0, 300, 300, fill = 'blue', width = 3)
di2 = canvas.create_line(300, 0, 0, 300, fill = 'red', width = 3)

root.mainloop()