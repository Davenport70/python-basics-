# Strings
# text and characters
# Syntax
# "" and ''

# Define a string
my_string = 'Hey I am a cool string B) '
print(my_string)

# check its type
print(type(my_string))

# concatenation
# adding of two strings
joint_string = my_string + 'This is another string'
print(joint_string)
# example two of concatenation
name = 'Mohammed'
welcome_text = 'THIS IS SPARTAA!'
print(welcome_text + ' ' + name)
print(welcome_text, name) # overloading the print method

# interpolation
# inserting a string inside another string
# or running python inside a string
print(f'WELCOME {input("What is your name?")} TO CLASS 54, WE ARE CONTESTED TERRAIN ')

print('WELCOME {} TO CLASS 54, we are contested terrain'.format(name))

# useful methods
# methods are like functions but belong to a specific data type
# for example, it would not make sense to try to capitalise integers
example_long_str = 'HELLO, ThIS is A VeRY bAD Formated text?     '
print(example_long_str)

# Remove trailling white space
print(example_long_str.strip())


# Make it lower case
print(example_long_str.lower())

# make it uppercase
print(example_long_str.upper())

# make only the first character capitalized
print(example_long_str.capitalize())

# make the first character of each word capitalized
print(example_long_str.title())

# change the '?' into a '!'
print(example_long_str.replace('?', '!'))

# chain some methods and:
# remove trailing white spaces
# make it nicely formated with only the first letter capitalised
print(example_long_str.strip().capitalize().replace('?', '!'))

# create a list