
# Examples of if statements
age = 13
if age > 20:
    print("You are too old!")
if age < 14:
    print("You are young enough!")

age = 25
if age > 20:
    print('You are too old!')
    print('Why are you here?')
    print('Why aren\'t you mowing a lawn or sorting papers?')

age = 10
if age == 10:
    print('What\'s brown and sticky? A stick!!')
if age >10:
    print('You are too old for my jokes!')

# Examples of if-else statement

print('Want to hear a dirty joke?')
age = 8
if age == 12:
    print("A pig fell in the mud!")
else:
    print("Shh. It's a secret.")

# Examples of if-elif (if-else-if) statements

age = 12
if age == 10:
    print('What do you call an unhappy cranberry?')
    print('A blueberry!')
elif age == 11:
    print("What did the green grape say to the blue grape?")
    print("Breathe!Breathe!")
elif age == 12:
    print("What did 0 say to 8?")
    print("Hi guys!")
elif age == 13:
    print("Why wasn't 10 afraid of 7?")
    print("Because rather than eating 9, 7, 8 pi.")
else:
    print("Huh?")

# Putting all on same line

age = 1

if age == 10 or age == 11 or age == 12 or age == 13:
    print("What is 13+ 49 +84 + 155 + 97? Aheadache!")
else:
    print("Huh?")

# Example of empty value, None

myVal = None # use it to reset a variable's original state, an empty state
if myVal == None:
    print("This variable myVal doesn't have a value.")

# Python treate all user inputs as string

age = 10
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")

age = '10'
converted_age_num = int(age) # convert string into number
converted_age_string = str(converted_age_num) # convert number into string
if converted_age_num == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")

# decimal number converter float()
