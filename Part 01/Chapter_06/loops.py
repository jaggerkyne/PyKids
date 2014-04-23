# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# for loop
# use for-loop when you know ahead of time how many steps you want to take.

for x in range(0,5): # not includsive of 5
    print("Hello ~~ %s" % x)

# using i as index
wizard_list = ['spider legs','toe if frog','snail tongue','bat wing','slug butter','bear burp']
for i in wizard_list:
    print(i)


hugehairypants = ['huge','hairy','pants']
for i in hugehairypants: # loop through the items in the list and each item is then assigned to the variable i
    print(i)
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3

coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week,coins))

# While-loop, use when you don't know the exact step ahead of time

# step = 0
# tired = False
# bad_weather = False
# while step < 10000:
#     print(step)
#     if tired == True:
#         break
#     elif bad_weather == True:
#         break
#     else:
#         step = step + 1

x = 45
y = 80

while x < 50 and y< 100:
    x = x + 1
    y = y + 1
    print(x,y)


# Semi-infinity loop using while
counter = 0
while True:
    counter = counter + 1
    if counter == 1:
        print ("I am the Truth! for the " + str(counter) + " time.")
    else:
        print ("I am the Truth! for the " + str(counter) + " times.")
    if counter == 100:
        break