# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import turtle
# while True:
#     avery = turtle.Pen()
#     kate = turtle.Pen()
#     avery.forward(50)
#     avery.right(90)
#     avery.forward(20)
#     kate.left(90)
#     kate.forward(100)
#     jacob = turtle.Pen()
#     jacob.left(180)
#     jacob.forward(80)
# Each class will be able to use the characteristics(functions) of its parent.

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


class Giraffes(Mammals):
    def __init__(self,spot): # set properties of an object when it is first created.
        self.giraffe_spots = spot

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

# introducing a giraffes named Reginald
reginald = Giraffes(20)
reginald.move()
reginald.eat_leaves_from_tree()
reginald.feed_young_with_milk()
reginald.find_food()
reginald.dance_a_jig()
reginald.eat_leaves_from_tree()

harold = Giraffes(30)
harold.move()

ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
