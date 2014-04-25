# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Race for the Exit")
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.canvas = Canvas(self.tk,width=500,height=500,highlightthickness=0)
        self.canvas.pack()
        self.canvas.update()
        self.canvas_height = 500
        self.canvas_width = 500
        bg_path = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/background.gif'
        self.bg = PhotoImage(file=bg_path)
        # test.gif
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0,5):
            for y in range(0,5):
                self.canvas.create_image(x*w,y*h,image=self.bg,anchor='nw')
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


class Corrds:

    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def within_x(co1,co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2)\
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2)\
            or (co2.x1 > co1.x1 and co2.x2 < co1.x1)\
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        return True
    else:
        return False

def within_y(co1,co2):
    if(co1.y1 > co2.y1 and co1.y1 <co2.y2)\
            or(co1.y2 > co2.y1 and co1.y2 < co2.y2)\
            or(co2.y1 > co1.y1 and co2.y1 < co1.y2)\
            or(co2.y2 > co1.y1 and co2.y2 < co1.y1):
        return True
    else:
        return False

def collided_left(co1,co2):
    if within_y(co1,co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

def collided_right(co1,co2):
    if within_y(co1,co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
         return True
    return False

def collided_top(co1,co2):
    if within_x(co1,co2):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False

def collided_bottom(y,co1,co2):
    if within_x(co1, co2):
        y_cal = co1.y2 + y
        if y_cal >= co2.y1 and y_cal <= co2.y2:
            return True
    return False

class Sprite:
    def __init__(self,game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates

class PlatformSprite(Sprite):
    def __init__(self,game,photo_image,x,y,width,height):
        Sprite.__init__(self,game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x,y,image=self.photo_image,anchor='nw')
        self.coordinates = Corrds(x,y,x + width, y + height)

g = Game()
path1 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/platform1.gif'
path2 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/platform2.gif'
path3 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/platform3.gif'
platform1 = PlatformSprite(g,PhotoImage(file=path1),0,480,100,10)
platform2 = PlatformSprite(g,PhotoImage(file=path1),150,440,100,10)
platform3 = PlatformSprite(g,PhotoImage(file=path1),300,480,100,10)
platform4 = PlatformSprite(g,PhotoImage(file=path1),300,160,100,10)
platform5 = PlatformSprite(g,PhotoImage(file=path2),175,350,66,10)
platform6 = PlatformSprite(g,PhotoImage(file=path2),50,380,66,10)
platform7 = PlatformSprite(g,PhotoImage(file=path2),170,120,66,10)
platform8 = PlatformSprite(g,PhotoImage(file=path2),45,60,66,10)
platform9 = PlatformSprite(g,PhotoImage(file=path3),170,250,32,10)
platform10 = PlatformSprite(g,PhotoImage(file=path3),230,280,32,10)

g.sprites.append(platform1)
g.mainloop()