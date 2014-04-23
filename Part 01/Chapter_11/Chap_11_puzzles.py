# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import turtle

#1: Drawing an Octagon

t = turtle.Pen() # get a pen from turtle module

def draw_an_octagon(size):

    for x in range(1,9):
        t.forward(size)
        t.left(45)


#2: Drawing a Filled Octagon

def draw_corlored_octagon(size,filled):
    t.color(0.9,0.4,0.2)
    if filled == True:
        t.begin_fill()
        draw_an_octagon(size)
    if filled == True:
        t.end_fill()

#3: Another star-drawing function

def draw_a_star(size,points):

    for x in range(1,points+1):
        t.forward(size)
        if x % 2 == 0:
            t.left(125)
        else:
            t.left(175)


while True:
    # draw_an_octagon(100)
    # draw_corlored_octagon(100,True)
    draw_a_star(100,17)
    pass
