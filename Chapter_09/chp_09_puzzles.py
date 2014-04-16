# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

import shutil

#1: Mystery code
def guess_num():
    a = abs(10) + abs(-10)
    print(a) # prints 20
    b = abs(-10) + -10
    print(b) # prints 0

guess_num()

#2: A hidden Message

def hidden_message():
    long_string = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
    after_splited = long_string.rsplit()
    length = len(after_splited)
    for i in range(0,length,2):
        print(after_splited[i])

hidden_message()

#3: Copying a file

def copying_a_file():
    # open a file
    original_file = open('/Chapter_09/test.txt')

    # read it in
    org_read = original_file.read()

    original_file.close()

    # create a new copy
    test_copy = open('/Chapter_09/test_copy.txt','w')

    test_copy.write(org_read)

    test_copy.close()

    print("Copied completed!")

copying_a_file()

def copy_in_Python_way():
    shutil.copy('test.txt','output.txt')
    print("Copy completed in Python's Way using shutil.copy().")

copy_in_Python_way()