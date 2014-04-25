# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_text(150,100, text = 'There once was a man from Toulouse',fill='red')
# canvas.create_text(300,200, Text="testing") What is Text for?
canvas.create_text(130,120,text='Who rode around on a moose?', fill='blue')

canvas.create_text(150,150,text="He said, 'It\'s my blessing,'", font=('Times',15))

canvas.create_text(200,200,text='But it could be worse,', font=('Helvetica',20))

canvas.create_text(220,250,text='My cousin rides around',font=('Courier',22))

canvas.create_text(220,300,text='On a goose.', font=('Courier',30))