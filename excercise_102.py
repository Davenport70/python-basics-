# # Create a little program that ask the user for the following details:
#  - Name
#  - height
#  - favourite color
#  - a secrete number

name = input('Hey what is your name?')
height = input('And what is your height?')
favorite_color = input('What is your favorite color?')
secret_number = input('Finally can you tell me a secret number')

print(f'''
Hello{name}, your height is{height}! wow!
Your favorite color is{favorite_color}, hey that is mine too! 
Finally your secret number is{secret_number}, shh I will keep it a secret.''')

# Capture these inputs
# Print a tailored welcome message to the user
# print other details gathered, except the secret of course

# hint, think about casting your data type.