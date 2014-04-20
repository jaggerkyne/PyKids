# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *
import random

tk=Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()

#draw an arc

# extent is used to specify the degree of the angle of the arc.
canvas.create_arc(10,10,200,80,extent=45, style=ARC)
canvas.create_arc(10,80,200,160,extent=90, style=ARC)
canvas.create_arc(10,160,200,240,extent=135, style=ARC)
canvas.create_arc(10,240,200,320,extent=180, style=ARC)
canvas.create_arc(10,320,200,400,extent=359, style=ARC)

