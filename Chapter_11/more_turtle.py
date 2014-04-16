# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


import turtle


def create_square_simple():
    t = turtle.Pen()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)

def create_square_advance():
    t = turtle.Pen()
    for x in range(1,5):
        t.forward(50)
        t.right(90)


def draw_a_eight_point_star():
    t = turtle.Pen()
    for x in range(1,21):
        t.forward(100)
        t.left(235)

def draw_somestar():
    t = turtle.Pen()
    for x in range(1,38):
        t.forward(100)
        t.left(175)

def draw_spiraling_star():
    t = turtle.Pen()
    for x in range(1,20):
        t.forward(100)
        t.left(95)

def draw_more_star():
    t = turtle.Pen()
    for x in range(1,19):
        t.forward(100)
        if x % 2 == 0: # divide things into 2 parts without any remainder.
            t.left(175)
        else:
            t.left(225)

def draw_colored_star(size, filled):
    t = turtle.Pen()
    t.color(0.7,0.25,0.45)
    if filled == True:
        t.begin_fill()
    for x in range(1,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    t.color(0,0,0)
    if filled == True:
        t.end_fill()

def draw_me_a_car():
    t = turtle.Pen()
    # draw a the body
    t.color(1,0,0)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.end_fill()

    # draw the first wheel

    t.color(0,0,0) # change the pen color color(Red,Green,Blue)
    t.up()
    t.forward(10)
    t.down()
    t.begin_fill() # start filling color
    t.circle(10) # draw a circle with radius at 10
    t.end_fill() # end filling color

    # draw the second wheel

    t.setheading(0)
    t.up()
    t.forward(90)
    t.right(90)
    t.forward(10)
    t.setheading(0) # turns the turtle to face a particular direction
    t.begin_fill()
    t.down()
    t.circle(10)
    t.end_fill()

def draw_a_colored_circle():
    t = turtle.Pen()
    t.color = (1,1,0) # 100% red, 100% Green, 0% Blue
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def draw_colored_circle(red,green,blue):
    t = turtle.Pen()
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(90)
    t.end_fill()

def draw_square(size,filled):
    t = turtle.Pen()
    if filled == True:
        t.begin_fill()
    for x in range(1,5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

while True:
    # create_square_simple()
    # create_square_advance()
    # draw_a_eight_point_star()
    # draw_somestar()
    # draw_spiraling_star()
    # draw_more_star()
    # draw_me_a_car()
    # draw_a_colored_circle()
    # draw_colored_circle(0,1,0) # draw a bright green circle
    # draw_colored_circle(0,0.5,0) # draw a dark green circle
    # draw_colored_circle(1,0,0) # full red
    # draw_colored_circle(0.5,0,0) #half red
    # draw_colored_circle(0,0,1) # full blue
    # draw_colored_circle(0,0,0.5) # half blue
    # draw_colored_circle(0.9,0.75,0) # gold circle
    # draw_colored_circle(1,0.7,0.75) # pink circle
    # draw_colored_circle(1,0.5,0) # orange
    # draw_colored_circle(0.9,0.5,0.15) # orange
    # draw_colored_circle(0,0,0) # pure black
    # draw_colored_circle(1,1,1) # all white
    # draw_square(10,True)
    # draw_square(25,False)
    # draw_square(50,True)
    # draw_square(75,False)
    # draw_square(100,True)
    # draw_square(125,False)
    # draw_square(150,True)
    draw_colored_star(20, False)
    draw_colored_star(40, True)
    draw_colored_star(60, False)


    pass