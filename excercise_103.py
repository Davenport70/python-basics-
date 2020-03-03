# Define the following variables
# name, last_name, species, eye_color, hair_color
name = 'Lana'
last_name = 'Jones'
species = 'Dog'
eye_color = 'black'
hair_color = 'green'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

name = input('Can I have your name please?')
last_name = input('Can I have your last name please?')
species = input('Can I have your species please?')
eye_color = input('Can I have your eye color please?')
hair_color = input('Can I have your hair color please?')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print('Hello {}! the {}! Welcome, your age is {}, your eyes are {} and your hair color is {}.'.format(name, last_name, species, eye_color, hair_color))