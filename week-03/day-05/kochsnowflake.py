from tkinter import *
from math import sqrt, pow
from time import sleep

root = Tk()

canvas_width = 600
canvas_height = 600
border = 2
canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = 'white')
canvas.pack()

def koch_line(x1, y1, x2, y2):

    if sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)) < 10:
        return

    # calculates the coordinates of the trisectional points
    x_third = (x2 - x1) / 3
    y_third = (y2 - y1) / 3
    first_trisectional_x = x1 + x_third
    first_trisectional_y = y1 + y_third
    second_trisectional_x = x1 + 2 * x_third
    second_trisectional_y = y1 + 2 * y_third

    # draws the base line
    canvas.create_line(x1, y1, first_trisectional_x, first_trisectional_y)
    canvas.create_line(first_trisectional_x, first_trisectional_y, second_trisectional_x, second_trisectional_y, fill = 'white', width = 3)
    canvas.create_line(second_trisectional_x, second_trisectional_y, x2, y2)
    # draws the peak triangle
    if y1 < y2: # downwards
        if x1 < x2: # rightwards
            canvas.create_line(first_trisectional_x, first_trisectional_y, x2, first_trisectional_y)
            canvas.create_line(x2, first_trisectional_y, second_trisectional_x, second_trisectional_y)
        elif x1 > x2: # leftwards
            canvas.create_line(first_trisectional_x, first_trisectional_y, x1, second_trisectional_y)
            canvas.create_line(x1, second_trisectional_y, second_trisectional_x, second_trisectional_y)
    elif y1 == y2: # horizontal base line, upwards and downwards is coded in the sign of the height 
        height = x_third * 3 / 4
        bisection_length = (x2 - x1) / 2
        canvas.create_line(first_trisectional_x, first_trisectional_y, x1 + bisection_length, y1 - height)
        canvas.create_line(x1 + bisection_length, y1 - height, second_trisectional_x, second_trisectional_y)
    else: # upwards
        if x1 < x2: # rightwards
            canvas.create_line(first_trisectional_x, first_trisectional_y, x1, second_trisectional_y) # only x2, y2 differ
            canvas.create_line(x1, second_trisectional_y, second_trisectional_x, second_trisectional_y) # detto
        elif x1 > x2: # leftwards
            canvas.create_line(first_trisectional_x, first_trisectional_y, x2, first_trisectional_y) # only x2, y2 differ
            canvas.create_line(x2, first_trisectional_y, second_trisectional_x, second_trisectional_y) # detto

    sleep(0.1)
    canvas.update()

    # calls function recursively for base line
    koch_line(x1, y1, first_trisectional_x, first_trisectional_y)
    koch_line(second_trisectional_x, second_trisectional_y, x2, y2)
    # calls function recursively for peak triangle
    if y1 < y2:
        if x1 < x2: # rightwards
            koch_line(first_trisectional_x, first_trisectional_y, x2, first_trisectional_y)
            koch_line(x2, first_trisectional_y, second_trisectional_x, second_trisectional_y)
        elif x1 > x2: # leftwards
            koch_line(first_trisectional_x, first_trisectional_y, x1, second_trisectional_y)
            koch_line(x1, second_trisectional_y, second_trisectional_x, second_trisectional_y)
    elif y1 == y2:
        height = x_third * 3 / 4
        bisection = (x2 - x1) / 2
        koch_line(first_trisectional_x, first_trisectional_y, x1 + bisection, y1 - height)
        koch_line(x1 + bisection, y1 - height, second_trisectional_x, second_trisectional_y)
    else:
        if x1 < x2: # rightwards
            koch_line(first_trisectional_x, first_trisectional_y, x1, second_trisectional_y) # only x2, y2 differ
            koch_line(x1, second_trisectional_y, second_trisectional_x, second_trisectional_y) # detto
        elif x1 > x2: # leftwards
            koch_line(first_trisectional_x, first_trisectional_y, x2, first_trisectional_y) # only x2, y2 differ
            koch_line(x2, first_trisectional_y, second_trisectional_x, second_trisectional_y) # detto


x1 = canvas_width
y1 = (canvas_height - border) / 4
x2 = canvas_width / 2
y2 = canvas_height

koch_line(x1, y1, x2, y2)
koch_line(x2, y2, border, y1)
koch_line(border, y1, x1, y1)


root.mainloop()