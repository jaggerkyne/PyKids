# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# The hello loop

for x in range(0,20):
    print('hello %s' % x)
    if x < 9:
        break

# # above code will loop through 0 and 19 and print out x, then it stops.

# # Even numbers
my_age = 32
for i in range(0,my_age+1):
    if i%2 == 0:
        print(i)


# My five favorite ingredients
# Method one
ingredients = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
counter = 0
for i in ingredients:
    counter = counter + 1
    print(str(counter) + " " + str(i))

# Method two
counter = 1
for j in ingredients:
    print('%s %s' % (counter, j))
    counter = counter + 1

# Your weight on the moon

# method one
weight_factor = 0.165
my_weight_on_earth = 70
weight_add_each_year = 1
year = 0

for year in range(0,15):
    year = year + 1
    my_weight_on_earth = my_weight_on_earth + 1
    moon_weight = my_weight_on_earth * weight_factor
    print ('Year %s and weight on the moon is %s' % (year,moon_weight))

# method two
my_weight = 70
for year in range(1,16):
    my_weight = my_weight + 1
    moon_weight = my_weight * 0.165
    # print( 'Year %s my moon weight is %s' % (year,moon_weight))
    print('Year %s is %s' % (year,moon_weight))