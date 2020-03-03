# practice string
# welcome to Sparta - excercise

# Version 1 specs
# define a variable name, and assign a string with a name

welcome = 'Hello and welcome!'
print(welcome)

# prompt the user for input and ask the user for his/her name

user_input = input('What is your name?')
print(user_input)

# use concatenation to print a welcome method and use method to format the name/input

print(f'Hello and welcome {user_input} thanks for the name!')

# version 2

# ask the user for a first name and save it as a variable

user_input_first_name = input('What is your first name?')
print(user_input_first_name)

# ask the user for a last name and save it as a variable
user_input_last_name = input('What is your last name?')
print(user_input_last_name)

# do the same but use a different message andza
# use interpolation to print the message

user_input_full_name = input('What is your first name') + ' ' + input('What is your last name')
print(user_input_full_name)

# Calculate year of Birth
# gather details on age and name
user_input_full_name = input('What is your first name') + ' ' + input('What is your last name')
age = input(f'Hello {user_input_full_name} can I take your age?')

birthday = 2020 - int(age)

input('Can I have your name please?')
print(f'OMG {user_input_full_name}, you are {age} years old so you were born in {birthday} year')
