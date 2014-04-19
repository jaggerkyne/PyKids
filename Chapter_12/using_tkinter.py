# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *
import random


def say_hello():
    print("Hello, my friend")

def create_a_button():
    tk = Tk() # create a basic windows to which we can add other things to it.
    btn = Button(tk,text="Click me", command=say_hello())
    btn.pack() # tells the button to appear


create_a_button()

# Using Named Parameters

def person(width, height):
    print("I am %s feet wide, %s feet high" %(width,height))

person(90,23)

person(height=40,width=80)

person(width=20,height=30)

# Creating a Canvas for Drawing using canvas object.

def create_canvas():
    tk = Tk()
    canvas = Canvas(tk,width=500,height=500) # specify the width and the height of the program
    canvas.pack() # display itself in the correct position within the windows.
    canvas.create_line(0,0,500,500) # draw a line from top left corner to bottom right corner.
    # returns 1, which is an identifier

# create_canvas()

def draw_a_box():
    tk = Tk()
    canvas = Canvas(tk,width=500,height=500) # specify the width and the height of the program
    canvas.pack() # display itself in the correct position within the windows.
    canvas.create_rectangle(10,10,50,50) # draw a square in the top-left corner of the window


def draw_a_rectangle():
    tk = Tk()
    canvas = Canvas(tk,width=500,height=500) # specify the width and the height of the program
    canvas.pack() # display itself in the correct position within the windows.
    canvas.create_rectangle(10,10,300,50) # draw a square in the top-left corner of the window

def draw_random_rectangles(width,height):
    tk=Tk()
    canvas = Canvas(tk,width=500,height=500)
    canvas.pack()
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)

draw_random_rectangles(400,400)