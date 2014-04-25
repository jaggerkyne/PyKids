# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from tkinter import *
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Checkerboard")
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.canvas = Canvas(self.tk,width=500,height=500,highlightthickness=0)
        self.canvas.pack()
        self.canvas.update()

        bg_path1 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/background.gif'
        bg_path2 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/background2.gif'
        lamp_path = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/lamp.gif'
        shelf_path = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/shelf.gif'

        self.bg = PhotoImage(file=bg_path1)
        self.bg2 = PhotoImage(file=bg_path2)
        self.bg_shelf = PhotoImage(file=shelf_path)
        self.bg_lamp = PhotoImage(file=lamp_path)

        w = self.bg.width()
        h = self.bg.height()

        count = 0

        draw_background = 0

        for x in range(0,5):
            for y in range(0,5):
                if draw_background == 1:
                    self.canvas.create_image(x*w,y*h,image=self.bg,anchor='nw')
                    draw_background = 0
                else:
                    count += 1
                    if count == 5:
                        self.canvas.create_image(x*w,y*h,image=self.bg_shelf,anchor='nw')
                    elif count == 9:
                        self.canvas.create_image(x*w,y*h,image=self.bg_lamp,anchor='nw')
                    else:
                        self.canvas.create_image(x*w,y*h,image=self.bg2,anchor='nw')
                    draw_background = 1

        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

game = Game()
game.mainloop()