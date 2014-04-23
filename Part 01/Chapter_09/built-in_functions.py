# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# The ABS function

print(abs(10)) # absolute value of a number

# The Bool function

print(bool(0))
# take a single parameter and returns either True or False based on its value.
# zero returns false, other number returns True.

bool(None) # return false
bool('String') # return true

#return false when list tuples and maps does not have value, return true when they do.

#Use bool when you need to decide whether a value has been set or not.

def bday_input():
    year = input('Year of birth:')
    if not bool(year.rstrip()): #rstrip removes any space and ENTER character from the end of the string.
        print("You need to enter a value for your year of birth.")

# bday_input()

dir([]) # dir function short for directory return information about any value.

# use dir() function when you have a variable and quickly want to find out what you can do with it.
#For example:
popcorn = 'I love popcorn'
dir(popcorn)

# The Eval function

#eval() # takes a string as a parameter and runs it as though it were a python expression.

# expression that are split over more than one line like if-else statement generally won't evaluate.

# eval() function is used to turn user input into python expression.

# for example:
def test_eval():
    your_calculation = input("Please enter a calculation:")
    eval(your_calculation)

# exec() function is like eval(),
# except that you can use it to run more complicated programs and does not return a value.

def exe_program():
    # my_small_program = '''print('ham'), print('sandwich')'''
    # exec(my_small_program)
    pass

# use exec() to execute mini programs within a big program

# float() function converts a string or a number into a floating-point number.
# int() function converts a string or a number into a whole number.
# len() function returns the length of an object.

# len() for string
def len_for_string():
    print(len('This is a test string'))

def len_for_list():
    creature_list = ['unicorn','cyclops','fairy','elf','dragon','troll']
    print(len(creature_list))

def len_for_map():
    enemies_map = {'Batman':'Joker','Superman':'Lex Luthor','Spiderman':'Green Goblin'}
    print(len(enemies_map))

def len_for_loop():
    fruit =['Apple','Banana','Clementine','Dragon fruit']
    length = len(fruit)
    for x in range(0,length):
        print('The fruit at index %s is %s' % (x,fruit[x]))

len_for_string()
len_for_list()
len_for_map()
len_for_loop()

#max() returns the largest item in a list, tuple or string and min() functions returns the smallest value.

# Letters are ranked alphabetically and the lower case letters comes after uppercase letters.

def guess_a_num():
    guess_this_num = 61
    player_guesses = [12,15,70,45]
    if max(player_guesses) > guess_this_num:
        print("Boom! You all lose")
    else:
        print('You win')

# range() function, range(start,stop,step),
# the numbers that range generates begin with the number given as the first parameter and end with the number than's
# one less than the second parameter.

# use range() with starting and stop point

def use_range():
    count_by_one = list(range(0,30)) # when step value is not used, the number 1 is used by default
    count_by_two = list(range(0,30,2))
    count_by_minus_two = list(range(40,10,-2))
    print(count_by_one)
    print(count_by_two)
    print(count_by_minus_two)
use_range()

def use_sum():
    my_list_of_numbers = list(range(0,500,50))
    print(my_list_of_numbers)
    print('The sum of my list of number is ' + str(sum(my_list_of_numbers)))

use_sum()

def open_testfile():
    #open a file
    test_file = open('/Chapter_09/test.txt')

    #write to file, letter w tells Python that we want to write the file object.
    test_file = open('/Chapter_09/test.txt','w')
    # write the string into the file object, replacing all existing content.

    test_file.write('This is my test file, ok?')

    # print(test_file.read())
    # close the writing to the object.
    test_file.close()

open_testfile()


