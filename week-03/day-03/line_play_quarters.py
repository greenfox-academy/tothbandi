
from tkinter import *

root = Tk()

c_width = 300
c_height = 300
canvas = Canvas(root, width=c_width, height=c_height, bg='white')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

number_of_rows = int(input("horizontal divison of canvas = munber of rows "))
number_of_columns = int(input("vertical divison of canvas = munber of columns "))
number_of_lines = int(input("number of lines in a division "))
h_div = c_height // number_of_rows # 150
v_div = c_width // number_of_columns  # 100

def line_play(tlx, tly, brx, bry, line_number):
    h_div = (bry - tly) // line_number
    v_div = (brx - tlx) // line_number
    for i in range(line_number):
            line = canvas.create_line(tlx + i*v_div, tly, brx, tly + i*h_div, fill='purple')
            line = canvas.create_line(tlx, tly + i*h_div, tlx + i*v_div, bry, fill='green')

for row in range(number_of_rows):
    for col in range(number_of_columns):
        line_play(col*v_div, row*h_div, (col+1)*v_div, (row+1)*h_div, number_of_lines)


root.mainloop()