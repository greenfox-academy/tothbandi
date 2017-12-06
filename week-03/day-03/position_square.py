from tkinter import *

root = Tk()

c_width, c_height = 300, 300
canvas = Canvas(root, width=c_width, height=c_height, bg = 'grey') 
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def sq(tlx, tly):
    r = canvas.create_rectangle(tlx, tly, tlx + 50, tly + 50, fill = 'yellow')

sq(-10, -10)
sq(210, 30)
sq(280, 290)

root.mainloop()