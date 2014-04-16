
# string
wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'

print(wizard_list)


# list

wizard_list = ['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff']

print(wizard_list)

print("The second item on the wizard list is " + wizard_list[2]) # should print out eye of newt

wizard_list[2] = 'snail tongue' # change eye of newt by snail tongue

print(wizard_list)

#print subset of the list

print(wizard_list[2:5]) # shoow the items from index position 2 up to (but not including) index position 5


# example of lists
some_numbers = [1,2,34,53,52,53,56]
some_strings = ['This is very', 'cool', 'you know']
mix_nums_and_strings = [1,24,56,74,'this is mine']
mylists = [some_numbers,some_strings,mix_nums_and_strings]

print(some_numbers)
print(some_strings)
print(mix_nums_and_strings)
print(mylists)


# Adding items to a list
wizard_list.append('bear burp') # append adds an item to the end of a list.
print(wizard_list)

wizard_list.append('herck')
wizard_list.append('Chicken legs')
wizard_list.append('Virgin tears')

print(wizard_list)

# Removing an item from a list

del wizard_list[0] # remove spider legs from the list
print(wizard_list)

# List Arithmetic

list_nums = [1,2,3,4,5]
list_strings = ['this is mine', 'Really?', 'Yes']
mix_list = list_nums + list_strings # Adding two lists
print(mix_list)
print(list_strings *10) # print the items inside the list 10 times and put them into one list

