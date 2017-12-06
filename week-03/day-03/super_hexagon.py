from tkinter import *
from math import sqrt
from time import sleep

root = Tk()

canvas = Canvas(root, width='600', height='600', bg='white')
canvas.pack()

main_diagonal = int(input("Number of hexagoncells in superhexagon main diagonal (3, 5, 7, ...): "))
cell_height = 600 // main_diagonal
cell_side = int(cell_height / sqrt(3))

def cell(x, y, ch, cs): # x, y = cell origo, ch: cell height, cs: cell side
    cell = canvas.create_polygon(
        x-cs, y, 
        x-cs/2, y-ch/2, 
        x+cs/2, y-ch/2, 
        x+cs, y, 
        x+cs/2, y+ch/2,
        x-cs/2, y+ch/2,
        fill='white',
        outline='black')
    sleep(0.2)
    canvas.update()
            # first cell origo position : 
x = 600 / 2 # horizontally in the middle
y = cell_height / 2 + 2 # vertically half cell height down
for i in range(main_diagonal, main_diagonal//2, -1):
    for j in range(i):
        cell(
            x + int(1.5*cell_side*(main_diagonal-i)), 
            y + j*cell_height + (main_diagonal-i)*cell_height//2, 
            cell_height, cell_side)
        cell(
            x - int(1.5*cell_side*(main_diagonal-i)), 
            y + j*cell_height + (main_diagonal-i)*cell_height//2, 
            cell_height, cell_side)


root.mainloop()