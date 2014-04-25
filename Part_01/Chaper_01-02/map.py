# a map is refered as dict, short for dictionary.
# key and value pair, key:value

favorite_sports_list = ['Ralph William, Football',
                    'Michael Jordan, Basketball',
                    'Eward Elgar, Baseball',
                    'Ethel Smyth, Badminton',
                    'Frank Bridge, Ruby']

print(favorite_sports_list)

favorite_sports_map = {'Ralph William':'Football',
                    'Michael Jordan':'Basketball',
                    'Eward Elgar':'Baseball',
                    'Ethel Smyth':'Badminton',
                    'Frank Bridge':'Ruby'}
print(favorite_sports_map)

print('Ethel Smyth likes to play ' + favorite_sports_map['Ethel Smyth'] + '.')

# remove Ethel Smyth
del favorite_sports_map['Ethel Smyth']
print(favorite_sports_map)

# replace a value in a map

favorite_sports_map['Ralph William'] = 'Ice Hockey' # replace Football by Ice Hockey
print(favorite_sports_map)
