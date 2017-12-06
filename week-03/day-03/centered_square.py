from tkinter import *

root = Tk()

c_width, c_height = 300, 300
canvas = Canvas(root, width=c_width, height=c_height, bg='white')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.

sq_width = 10
sq_height = 10
print((c_width - sq_width) // 2)
print((c_width + sq_width) // 2)
fx = (c_width - sq_width) // 2
fy = (c_height - sq_height) // 2
tx = (c_width + sq_width) // 2
ty = (c_width + sq_width) // 2
line = canvas.create_rectangle(fx, fy, tx, ty, fill='orange')

root.mainloop()