from tkinter import *

root = Tk()

c_width, c_height = 300, 300
canvas = Canvas(root, width=c_width, height=c_height, bg ='white')
canvas.pack()

# draw four different size and color rectangles.

r1 = canvas.create_rectangle(15, 43, 180, 150, fill = 'red')
r2 = canvas.create_rectangle(30, 150, 80, 290, fill = 'blue')
r1 = canvas.create_rectangle(100, 111, 200, 200, fill = 'green')
r1 = canvas.create_rectangle(150, 150, 180, 200, fill = 'gray')



root.mainloop()