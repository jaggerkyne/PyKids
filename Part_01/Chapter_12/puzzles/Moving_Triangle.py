# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 2 The moving Triangle
# move the triangle to right, down, back and left, to original position
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=800,height=600)
canvas.pack()
triangle = canvas.create_polygon(10,10,10,60,50,35)

# canvas.move(identifier,x,y)
# for x axis, back is negative, forward is positive
# for y axis, down is positive, up is negative

for x in range(0,60):
    # move to right
    canvas.move(1,10,0)
    tk.update()
    time.sleep(0.05)

for x in range(0,14):
    #move down
    canvas.move(1,0,10)
    tk.update()
    time.sleep(0.05)

for x in range(0,30):
    #move back
    canvas.move(1,-10,0)
    tk.update()
    time.sleep(0.05)
for x in range(0,15):
    #move back to original
    canvas.move(1,0,-10)
    tk.update()
    time.sleep(0.05)
