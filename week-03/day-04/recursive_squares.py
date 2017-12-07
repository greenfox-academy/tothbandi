from tkinter import *

root = Tk()

c_width = 600
c_height = 600
canvas = Canvas(root, width=c_width, height=c_height, bg='yellow')
canvas.pack()

def draw_squares(x1, y1, x2, y2):
    d = (x2 - x1) // 3
    line = canvas.create_line(x1+d, y1, x1 + d, y2)
    line = canvas.create_line(x1+2*d, y1, x1 + 2*d, y2)
    line = canvas.create_line(x1, y1 + d, x2, y1 + d)
    line = canvas.create_line(x1, y1 + 2*d, x2, y1 + 2*d)
    if d < 5:
        return
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 != 0:
                draw_squares(x1 + j * d, y1 + i * d, x1 + (j + 1) * d, y1 + (i + 1) * d)

draw_squares(0,0, c_width, c_height)

root.mainloop()