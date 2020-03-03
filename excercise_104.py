# Define the following variables
# name, last_name, species, eye_color, hair_color, age
# name = 'Lana'

name = 'Lana'
last_name = 'Jones'
species = 'Dog'
eye_color = 'black'
hair_color = 'green'
age = 50

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

name = input('What new name would you like?')
last_name = input('What new last name would you like?')
species = input('What new species would you like?')
eye_color = input('What new eye color would you like?')
hair_color = input('What new hair color would you like?')
age = input('What is your new age?')

## Calculate year of birth
# import time
# calculate the difference

import time
birthday = (2020 - int(age))

# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'

print('Hello {} {}! Welcome, your species is {}, your eyes are {} and your hair color is {}.'.format(name, last_name, species, eye_color, hair_color))
print('You said you were {}, if you have already had your birthday that means you were born in {}'.format(age, birthday))
# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age

age = input('Can I have your age?')
name = input('Can I have your name?')
mothers_name = input('Can I have your mothers name?')
mothers_age = input('Can I have your mothers age?')
difference = int(mothers_age) - int(age)

print('your mother, {} is {} and you are {} {}, I know your mother is {} older that you'.format(mothers_name, mothers_age, age, name, difference))

# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>. This is <difference_y> later than <mom_name> who was on on <y_birth_mon>