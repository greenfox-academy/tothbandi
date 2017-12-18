from tkinter import *
import tile
import maps

root = Tk()
canvas = Canvas(root, width = 724, height = 724)
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
            print('0')
            tiles[i].append(tile.Floor(4 + j * 72, 4 + i * 72))
            images[i].append(PhotoImage(file = tiles[i][j].image))
            canvas.create_image(tiles[i][j].posx, tiles[i][j].posy, anchor = 'nw', image = images[i][j])
        else:
            tiles[i].append(tile.Wall(4 + j * 72, 4 + i * 72))
            print(tiles[i][j].image)
            images[i].append(PhotoImage(file = tiles[i][j].image))
            canvas.create_image(tiles[i][j].posx, tiles[i][j].posy, anchor = 'nw', image = images[i][j])
            
root.mainloop()