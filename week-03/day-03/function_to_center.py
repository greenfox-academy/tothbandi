from tkinter import *

root = Tk()

c_width = 300
c_height = 300
canvas = Canvas(root, width=c_width, height=c_height, bg='white')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

center_x = c_width // 2
center_y = c_height // 2

def draw_line(fx, fy):
    line = canvas.create_line(fx, fy, center_x, center_y)

for i in range(0, c_width + 1, 20):
    draw_line(i, 0)
    draw_line(i, c_height)
for i in range(0, c_height + 1, 20):
    draw_line(0, i)
    draw_line(c_width, i)

root.mainloop()