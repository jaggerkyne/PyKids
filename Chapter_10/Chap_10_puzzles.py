# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import copy
import pickle

#1: Copied Cards

class Car:
    pass

def copy_car():
    car_1 = Car()
    car_1.wheels = 4
    car_2 = car_1
    car_2.wheels = 3
    print(car_1.wheels) # print out 3 instead of 4 because car_2 and car_1 are pointed to the same object
    car_3 = copy.copy(car_1) #copy.copy() creates a copy of the object.
    car_3.wheels = 6
    print(car_1.wheels) #print out 3

copy_car()

#2: Pickled Favorites

def using_pickle():
    my_favors = {"games":['software development','Eat Burger','Chinese KongFu']
    }

    # save file into binary
    save_file = open('saved_favors.dat','wb') # prepare for writing binary
    pickle.dump(my_favors,save_file) # write my_favors into a binary file named saved_favors.dat
    save_file.close()

    # read the binary and load it back to readable format
    load_file = open('saved_favors.dat','rb') #converts it back into values that our program can use. 'rb' means read binary.
    localed_my_favors_data = pickle.load(load_file)
    load_file.close()

    #print out the result.
    print(localed_my_favors_data)

using_pickle()