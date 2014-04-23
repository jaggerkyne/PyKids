# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# Making copies with the copy module
import copy

# Using keyword module
import keyword

# Using random module
import random

# Using sys module
import sys

# Using time module
import time

# Using the Pickle module
import pickle

class Animal:
    def __init__(self,species,number_of_legs,color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

def using_copy_module():
    harry = Animal('hippogriff',6,'pink')
    carrie = Animal('chimera',4,'green polka dots')
    billy = Animal('bogill',0,'paisley')
    my_animals = [harry, carrie,billy]
    more_animals = copy.copy(my_animals)
    harriet = copy.copy(harry)
    print(harry.species)
    print(harriet.species)
    print(more_animals[0].species)
    print(more_animals[1].species)
    my_animals[0].species = 'ghoul'
    print(my_animals[0].species)

    sally = Animal('sphinx',4,'sand')
    my_animals.append(sally)
    print(len(my_animals))
    print(len(more_animals))

# using_copy_module()

# deepcopy() creates copies of all objects inside the object being copied.
def using_deepcopy():
    harry = Animal('hippogriff',6,'pink')
    carrie = Animal('chimera',4,'green polka dots')
    billy = Animal('bogill',0,'paisley')
    my_animals = [harry, carrie,billy]
    my_animals[0].species = 'ghoul'
    more_animals = copy.deepcopy(my_animals)
    my_animals[0].species = 'wyrm'
    print(my_animals[0].species)
    print(more_animals[0].species)

# using_deepcopy()

# keeping track of keywords with the keyword module
# a Python keywords is any word in python that is part of the language itself.

# function iskeyword() returns true if any string is a python keyword

def keyword_verify(test_keyword):

    print('Is ' + str(test_keyword) + ' a keyword? ' + str(keyword.iskeyword(test_keyword)))



# keyword_verify('if')
# keyword_verify('ozwald')

# Variable kwlist returns a list of all Python keywords.

def print_keyword_list(test_keyword):

    print(test_keyword.kwlist)


# print_keyword_list(keyword)

# Getting random numbers with the random module
# most random modules are randint, choice and shuffle.

# randint() picks a random number between a range of numbers, say between 1 and 100

def pick_a_random_num():
    print(random.randint(1,100))
    print(random.randint(100,1000))
    print(random.randint(1000,9000))

# pick_a_random_num()

def random_game():
    num = random.randint(1,100)
    while True:
        print("Guess a number between 1 and 100!")
        guess = input()
        i = int(guess)
        if i == num:
            print("Yes, you are right!")
            break
        elif i < num:
            print("Try a bit higher!")
        elif i > num:
            print("Try lower!")

# random_game()

# Using choice to pick a random item from a list using choice() function.

def pick_random_item():
    desserts = ['ice cream', 'pancakes','brownies','cookies','candy']
    print("Let's pickup a desserts " + str(random.choice(desserts)) + '!')

# pick_random_item()

# using shuffle() to shuffle a list

def shuffle_a_list():
    desserts = ['ice cream', 'pancakes','brownies','cookies','candy']
    print('My wife wants to eat deserts in this order: ' + str(desserts))
    random.shuffle(desserts)
    print('I want to eat deserts in this order: ' + str(desserts))

# shuffle_a_list()

# Controlling the shell with the sys module
# import sys
# sys.exit()

# Reading with the stdin Object short for standard input object in the sys module prompts a user to enter information
# to be read into the shell and used by the program.

def test_readline():
    print("Enter Something Interesting!")
    # readline() function is used to read a line of text typed on the keyboard until the
    # the user press ENTER
    user_input = sys.stdin.readline() # allows string and numbers
    print('You just entered: ' + user_input)

# test_readline()

def test_input():
    print("Enter some interesting numbers")
    user_input = input() # input() returns int or float
    print(user_input)

def test_raw_input():
    print("Enter something interesting!")
    # user_input = raw_input() # raw_input() returns string, raw_input() is replaced by input() in python 3
    # print(user_input)

# Writing with the stdout object short for standard output can be used to write message to the shell or console.
# stdout is similar to print, but it is a file object.

def test_stdout():
    sys.stdout.write("What does a fish say when it is swims into a wall? Dam.")

# test_stdout()

def test_python_version():
    print(sys.version) # print out python version

# Doing time with the time module

def print_time():

    print(time.time()) # time() returns the number of seconds since Jan 1 1970 at: 00:00:00 AM

# print_time()

def test_time_take_to_run(max):
    initial_time = time.time()
    for x in range(0,max):
        print(x)
        time_gap = time.time()
        print('It took %s second' % (time_gap-initial_time))

# test_time_take_to_run(100000)

# Converting a Date with ASCTime
def convert_time():
    print(time.asctime())
    t =(2007,5,27,10,30,48,6,0,0)
    #(yyyy-mm-dd-hh-mm-ss-Date-date_of_the_year-if_daylight_saving)
    #date_of_the_year ->0 is a place holder
    #if_daylight_saving -> 0 if it isn't, 1 if it is.
    print(time.asctime(t))
# convert_time()

# Getting the date and time with localtime

def get_local_time():
    t = time.localtime()
    print(t)
    year = t[0]
    month = t[1]
    print(year)
    print(month)

# get_local_time()

# Taking some time off with sleep
def take_time_to_sleep():
    for x in range(1,61):
        print(x)
        time.sleep(1) # this will adds a delay between the display of each number.

# take_time_to_sleep()

# Using the pickle module to save information
# Pickle module is used to convert python objects into something that can be written into a file and then
# easily read back out.
def use_pickle_module():
    game_data = {
        'player-position':'N23 E45',
        'pockets':['key','pocket knife','polished stone'],
        'backpack':['rope','hammer','apple'],
        'money':158.50
    }
    save_file = open('save.dat','wb') #'wb' means write binary.
    pickle.dump(game_data,save_file) # save into binary data.
    save_file.close()
    load_file = open('save.dat','rb') #convert it back into values that our program can use. 'rb' means read binary.
    localed_game_data = pickle.load(load_file)
    load_file.close()
    print(localed_game_data)

use_pickle_module()