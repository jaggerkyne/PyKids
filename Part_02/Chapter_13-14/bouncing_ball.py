# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'



from tkinter import *
import random
import time

tk = Tk()
tk.title("!!Bounce!!") # windows title
tk.resizable(0,0) # size of the window cannot be changed either horizontally or vertically.
tk.wm_attributes("-topmost",1) # tell this game window is on top of everything else
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0) # no border around the outside of the canvas
canvas.pack()
tk.update() # tells tkinter to initialize itself itself for the animation in our game.


# create the ball class takes parameters for the canvas and color of the ball
class Ball:
    def __init__(self,canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color) # create a ball
        self.canvas.move(self.id,245,100) # move the oval to the middle of the canvas
        # self.x = 0 # 0 tell the ball does not move horizontally,
        # self.y = -1 # and the -1 says move 1 pixel up
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width =self.canvas.winfo_width()
        self.hit_bottom = False


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)  # don't move ball horizontally, 1 pixel up
        pos = self.canvas.coords(self.id) # returns the current x and y coordinate of current object drawn on the canvas
        # print(pos)# print out the coordinate
        if pos[1] <= 0: # top left coordinate of the ball hit the top
            self.y = 3 # bounce back down
        # Check if the ball hits the paddle
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[3] >= self.canvas_height: # bottom right coordinate of the ball
            # self.y = -3 # bounce back up
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3 # Left bounce
        if pos[2] >= self.canvas_width:
            self.x = -3 # right bounce

# check if the ball hits the paddle.
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

# Creating a Paddle class
class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width =self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0) # y coordinate is set
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -3

    def turn_right(self,evt):
        self.x = 3


paddle = Paddle(canvas,'blue')

ball = Ball(canvas,paddle,'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)