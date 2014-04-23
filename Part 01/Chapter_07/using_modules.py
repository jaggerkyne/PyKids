# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


import time
import sys

print(time.asctime()) # return current date and time as a string

# stdin: standard input
# readline() is used to read a line of text type of the keyboard until you press ENTER
print(sys.stdin.readline())

def silly_age_joke(age):
    print("How old are you?")
    age = int(sys.stdin.readline())
    if age >= 10 and age <=13:
        print("What is 13 + 49 + 84 + 155 + 97? \nA headache!")
    else:
        print("Huh?")

silly_age_joke(11)