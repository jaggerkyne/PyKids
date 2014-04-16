# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from tkinter import *


def say_hello():
    print("Hello, my friend")

def create_a_button():
    tk = Tk() # create a basic windows to which we can add other things to it.
    btn = Button(tk,text="Click me", command=say_hello())
    btn.pack() # tells the button to appear


create_a_button()