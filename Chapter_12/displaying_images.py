# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk,width =500, height=600)
canvas.pack()
# load the image,
# my_image = PhotoImage(file='sonic.gif') # somehow the link address is invalid
# photoImage() only support gif and PGM/PPM formats, if you want to use jpg, you need to
# use "from PIL import Image, ImageTk"
samuel = PhotoImage(file='/Users/Wilson/Documents/Sites/Python_For_Kids/Chapter_12/test.gif')

# If the images store in a particular folder, what should I write for the address?

# use create_image on the canvas object.
# canvas.create_image(0,0,anchor=NW,image=my_image)
canvas.create_image(0,0,anchor=NW,image=samuel)
for x in range(0,60):
    canvas.move(1,10,10)
    tk.update()
    time.sleep(0.05)




