# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


list(range(0,5))

def testfunc(myname):
    print('hello %s' % myname)

testfunc('Wilson')

def sayhello(fname,lname):
    print('Hello, %s %s' % (fname,lname))

sayhello("Wilson", 'Yang')

# first_name = raw_input("Please enter your first name!")
# last_name =raw_input("What is your last name?")
#
# sayhello(first_name,last_name)

def savings(pocket_money,paper_route,spending):
    return paper_route + pocket_money - spending

print(savings(10,10,5))

def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable

print(variable_test())

def spaceship_building(cans):
    total_cans = 0
    for week in range(1,53):
        total_cans = total_cans + cans
        print('week %s = %s cans' % (week,total_cans))

print(spaceship_building(2))

# Functions can be grouped together into modules.