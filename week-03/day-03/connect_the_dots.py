
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

l1 = [[10, 10], [290,  10], [290, 290], [10, 290]]
l2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

def connect_points(l, color):
    for i in range(len(l)-1):
        line = canvas.create_line(l[i][0], l[i][1], l[i+1][0], l[i+1][1], fill = color)
    line = canvas.create_line(l[0][0], l[0][1], l[len(l)-1][0], l[len(l)-1][1], fill = color)

connect_points(l1, 'red')
connect_points(l2, 'green')

root.mainloop()