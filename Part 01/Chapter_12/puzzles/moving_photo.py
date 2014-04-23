# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


import time
from tkinter import *
# from PIL import Image, ImageTk
tk = Tk()
canvas = Canvas(tk,width=800,height=600)
canvas.pack()
# PhotoImage() only supports GIF and PGM/PPM
samuel = PhotoImage(file='/Users/Wilson/Documents/Sites/Python_For_Kids/Chapter_12/test.gif')
canvas.create_image(0,0,anchor=NW,image =samuel)

for x in range(0,60):
    canvas.move(1,10,10)
    tk.update()
    time.sleep(0.05)