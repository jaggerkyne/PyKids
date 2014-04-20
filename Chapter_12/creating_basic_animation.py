# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import time

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 800, height=600)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    # canvas.move(1,5,0) # move object id 1, 5 pixels across and 0 pixels down.
    canvas.move(1,10,8)
    tk.update() # update the screen, redrawing, this gives the animation effect
    time.sleep(0.1) # time between each move, it is 0.1seconds in this case.

for x in range(0,60):
    canvas.move(1,-5,-5)
    tk.update()
    time.sleep(0.05)