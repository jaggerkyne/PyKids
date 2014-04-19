# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from tkinter import *
tk = Tk()
canvas = Canvas(tk,width =500, height=600)
canvas.pack()
# load the image,
my_image = PhotoImage(file='/Chapter_12/sonic.gif')
# use create_image on the canvas object.
canvas.create_image(0,0,anchor=NW,image=my_image)





