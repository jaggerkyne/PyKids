found_coins = 20
magic_coins = 10
stolen_coins = 2

total_coins_after_a_year = found_coins + magic_coins * 365 - stolen_coins * 52
print(total_coins_after_a_year)


# Silly String with excapte \ symbol. '

silly_string = 'He said, "Aren\'t can\'t wouldn\'t."'

print(silly_string)

# Silly string with triple quote

silly_string_2 = '''He said, "Aren\'t can\'t wouldn\'t." '''

print(silly_string_2)

single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'

print(single_quote_str)

double_quote_str = "He said, \"Aren't can\'t shouldn\'t wouldn\'t.\""

print(double_quote_str)

# Embededing values in a string with '%s'

myscore = 1000
message = "I scored %s points"
print(message % myscore)

joke_text = '%s: a device for finding furniture in the dark'
bodypart1= 'Knee'
bodypart2= 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)

# muiltiple placeholders
nums = 'What did the number %s say to the number %s? Nice belt!!'

print(nums % (0,8))

# muiltiplying strings
str =  'a'
print(10 * str)


