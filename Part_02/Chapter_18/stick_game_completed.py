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
        bg_path = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_16/graphics/background2.gif'
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


class Coords:
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def within_x(co1,co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2)\
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2)\
            or (co2.x1 > co1.x1 and co2.x2 < co1.x2)\
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
        self.coordinates = Coords(x,y,x + width, y + height)


class StickFigureSprite(Sprite):
    def __init__(self,game):
        Sprite.__init__(self,game)
        stick_figure_path1= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_L_1.gif'
        stick_figure_path2= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_L_2.gif'
        stick_figure_path3= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_L_3.gif'
        stick_figure_path4= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_R_1.gif'
        stick_figure_path5= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_R_2.gif'
        stick_figure_path6= '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/figure_R_3.gif'
        self.images_left =[
            PhotoImage(file=stick_figure_path1),
            PhotoImage(file=stick_figure_path2),
            PhotoImage(file=stick_figure_path3)
        ]
        self.images_right =[
            PhotoImage(file=stick_figure_path4),
            PhotoImage(file=stick_figure_path5),
            PhotoImage(file=stick_figure_path6)
        ]
        self.image = game.canvas.create_image(200,470,image=self.images_left[0],anchor='nw')

        # negative x value mean move left on the screen, positive x value mean move to right
        # negative y value mean move up, and positive y value mean move down

        self.x = -2 # move 2 pixel to the left on the screen
        self.y = 0

        self.current_image = 0 # current image's index position
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords() # stick figure's initial position

        # key bindings
        game.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        game.canvas.bind_all('<space>',self.jump)

    # actions taken by stick figure to the left
    def turn_left(self,evt):
        if self.y == 0:
            self.x = -2

    # actions taken by stick figure to the right
    def turn_right(self,evt):
        if self.y == 0:
            self.x = 2

    # actions taken by stick figure to the jump
    def jump(self,evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0 # use jump_count to make sure the stick figure doesn't keep jumping forever.

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.01:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0: # figure moves left
            if self.y != 0: # jumping
                self.game.canvas.itemconfig(self.image,image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image,image=self.images_left[self.current_image])
        elif self.x > 0: # figure moves right
            if self.y !=0:
                self.game.canvas.itemconfig(self.image,image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image,image=self.images_right[self.current_image])

    def coords(self):
        xy = list(self.game.canvas.coords(self.image))
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1

        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True

        # check if the stick figure hits the bottom of the canvas
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        # check if the stick figure hits the top of the canvas
        elif self.y < 0 and co.y1 <=0:
            self.y =0
            top = False
        # check if the stick figure runs to the left
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0 # stop the stick figure from running
            right = False

        # check if the stick figure runs to the right
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co,sprite_co):
                self.y = -self.y
                top = False
        if bottom and self.y > 0 and collided_bottom(self.y,co,sprite_co):
            self.y = sprite_co.y1 - co.y2
            if self.y < 0:
                self.y = 0
            bottom = False
            top = False
        if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1,co,sprite_co):
            falling =False
        if left and self.x < 0 and collided_left(co,sprite_co):
            self.x = 0
            left = False
        if right and self.x > 0 and collided_right(co, sprite_co):
            self.x = 0
            right = False
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y =4
        self.game.canvas.move(self.image,self.x,self.y)





g = Game()
path1 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/platform1.gif'
path2 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/platform2.gif'
path3 = '/Users/Wilson/Documents/Sites/Python_For_Kids/Part_02/Chapter_17/graphics/platform3.gif'
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
sf = StickFigureSprite(g)
g.sprites.append(sf)
g.mainloop()
