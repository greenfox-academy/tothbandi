from tkinter import *
from resizeimage import resizeimage
import tile
import maps

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() - 168 # because of Windows taskbar
atile = tile.Floor(0,0)
img = PhotoImage(file = atile.image)

board_width = 10 * img.width()
board_height = 10 * img.height()

width_ratio = screen_width / board_width
if width_ratio > 1.0:
    width_ratio = 1.0
height_ratio = screen_height / board_height
if width_ratio > 1.0:
    width_ratio = 1.0
ratio = width_ratio if width_ratio < height_ratio else height_ratio
canvas_width = board_width * ratio + 4
canvas_height = board_height * ratio + 4

print(ratio)

print(str(board_width * ratio) + ' ' + str(board_height *ratio))

canvas = Canvas(root, width = canvas_width, height = canvas_height)
print(canvas)
canvas.pack()
a_map = maps.Maps()
area = a_map.get_map()
tiles = []
global images
images = []

for i in range(10):
    tiles.append([])
    images.append([])
    for j in range(10):
        if area[i][j] == '0':
            tiles[i].append(tile.Floor(4 + j * 72, 4 + i * 72))
            images[i].append(PhotoImage(file = tiles[i][j].image))
            iid = canvas.create_image(tiles[i][j].posx, tiles[i][j].posy, anchor = 'nw', image = images[i][j])
            canvas.scale(iid, 0, 0, ratio, ratio)
        else:
            tiles[i].append(tile.Wall(4 + j * 72, 4 + i * 72))
            images[i].append(PhotoImage(file = tiles[i][j].image))
            iid = canvas.create_image(tiles[i][j].posx, tiles[i][j].posy, anchor = 'nw', image = images[i][j])
            canvas.scale(iid, 0, 0, ratio, ratio)
root.mainloop()