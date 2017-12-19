from tkinter import *

class View(object):
    def __init__(self):
        self.root = Tk()
    
    def set_canvas_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight() - 168 # because of Windows taskbar
        print('set_canvas_size')