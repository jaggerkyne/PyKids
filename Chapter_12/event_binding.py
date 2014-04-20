# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# event binding, lets an object to react when someone press a key.

# Events are things that occur while a program is running.

import time

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 800, height=600)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

def move_triangle(event):
  if event.keysym == 'Up':
      canvas.move(1,0,-3)
  elif event.keysym == 'Down':
      canvas.move(1,0,3)
  elif event.keysym == 'Left':
      canvas.move(1,-3,0)
  else:
      canvas.move(1,3,0)

# canvas.bind_all('<KeyPress-Return>',move_triangle()) #<KeyPress-Return> is an event
canvas.bind_all('<KeyPress-Up>',move_triangle) # use move_triangle instead of move_triangle()
canvas.bind_all('<KeyPress-Down>',move_triangle)
canvas.bind_all('<KeyPress-Left>',move_triangle)
canvas.bind_all('<KeyPress-Right>',move_triangle)
