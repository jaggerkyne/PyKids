# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *
import random

tk=Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()

#draw an arc

# below draws a triangle.
canvas.create_polygon(10,10,100,10,100,110,fill='',outline="black")
canvas.create_polygon(200,10,240,30,120,100,140,120,fill='',outline="pink")

