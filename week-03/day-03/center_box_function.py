from tkinter import *

root = Tk()

c_width, c_height = 300, 300
canvas = Canvas(root, width=c_width, height=c_height, bg='white')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def center_box(size):
    sq_width = size
    sq_height = size
    fx = (c_width - sq_width) // 2
    fy = (c_height - sq_height) // 2
    tx = (c_width + sq_width) // 2
    ty = (c_width + sq_width) // 2
    box = canvas.create_rectangle(fx, fy, tx, ty, fill = 'purple')
    
center_box(200)
center_box(100)
center_box(50)

root.mainloop()
