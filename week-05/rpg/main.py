from tkinter import *
import tile

root = Tk()
canvas = Canvas(root, width = 724, height = 724)
canvas.pack()


floor = []
for i in range(10):
    floor.append([])

    for j in range(10):
        floor[i].append(tile.Floor('floor.png', 2 + j * 72, 2 + i * 72))
        img = PhotoImage(file = floor[i][j].image)
        canvas.create_image(floor[i][j].posx, floor[i][j].posy, anchor = 'nw', image = img)

root.mainloop()