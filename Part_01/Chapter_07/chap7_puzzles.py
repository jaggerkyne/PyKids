# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import sys
#1: Basic Moon weight function

def moon_weight(initial_weight,weight_gain_each_year):

    for year in range(1,16):
        initial_weight = initial_weight + weight_gain_each_year
        moon_weight = initial_weight * 0.165
        print('Year %s is %s' % (year,moon_weight))

moon_weight(40,0.5)

#2: Moon weight function and years

def moon_weight_years(initial_weight,weight_gain_each_year,number_of_years):
    for year in range(1,number_of_years+1):
        initial_weight = initial_weight + weight_gain_each_year
        moon_weight = initial_weight * 0.165
        print('Year %s is %s' %(year, moon_weight))

moon_weight_years(35,0.3,5)


#3: Moon weight program

def moon_weight():
    print("What is your current weight?")
    initial_weight = int(sys.stdin.readline())
    print("How much weight you expect to grow each year?")
    weight_gain_each_year = float(sys.stdin.readline())
    print("How many year you are living on the moon?")
    years = int(sys.stdin.readline())
    
    moon_weight_years(initial_weight,weight_gain_each_year,years)


moon_weight()