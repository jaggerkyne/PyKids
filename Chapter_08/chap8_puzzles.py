# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


class Things:
    pass # use pass when not filling the details


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Sidewalks(Inanimate):
    pass


class Animals(Animate):

    def breathe(self):
        print('Breathing')

    def move(self):
        print('Moving')

    def eat_food(self):
        print('Eating food!')


class Mammals(Animals): # Mammals is type of Animals
    def feed_young_with_milk(self):
        print('feeding young')

#1: The Giraffe Shuffle

class Giraffes(Mammals):

    def __init__(self,spot): # set properties of an object when it is first created.
        self.giraffe_spots = spot

    def left_foot_forward(self):
        print('left foot forward')

    def left_foot_back(self):
        print('left foot back')

    def right_foot_forward(self):
        print('right foot forward')

    def right_foot_back(self):
        print('right foot back')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()

    def eat_leaves_from_tree(self):
        self.eat_food()

    def dance_a_jig(self):
        self.move() #Inherited functions are from the parent
        self.move()
        self.move()
        self.move()

    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

reginald = Giraffes(100)
reginald.dance()

#2: Turtle Pitchfork, chap8_task2_turtle_pitchfork

