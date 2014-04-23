# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# Fill the screen with triangles

from tkinter import *
import random

# Create canvas for painting first
w = 600
h = 800
tk = Tk()
canvas = Canvas(tk,width=w,height=h)
canvas.pack()
colors = ['red','blue','yellow','orange','purple','white']

# draw the triangles.
def createTriangles():

    # point 1
    x1 = random.randrange(w)
    y1 = random.randrange(h)

    # point 2
    x2 = random.randrange(w)
    y2 = random.randrange(h)

    # point 3
    x3 = random.randrange(w)
    y3 = random.randrange(h)
    color = random.choice(colors)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=color,outline="black")


for x in range(1,100):
    createTriangles()


