# Magic number game!
# I want you to use operators
# equate something
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# We should define/assign number to a variable called magic_number
# magic_number =


# import random
import random

# need 1 random number
magic_number = random.randint(1, 25)

# need one user input
guess = int(input('Enter a number between 1 and 25: '))
# evaluate using comparision operators user input vs number

if guess == magic_number:
    print('You got it!')
else:
    print('wrong try again')

    # this should result in true or false

# print if our response was correct
# 'your response was correct? <variable_with_boolean>'






#
# magic_number = random.randint(1,25)
# print(magic_number)
#
# guess = input("Pick a number between 1 and 25: ")
# counter = 0
#
# while counter < 5:
#     if guess != magic_number:
#         counter += 1
#         input("Unlucky! Try again! ")
#     elif guess == magic_number:
#         print("Congratulations!")
#         counter += 1
#     print('whoooohhwhwh')



# I need to ask user for input
#
# def guess():
#     counter = 0
#     guess = input("Pick a number between 1 and 25: ")
#     print(guess)
#     print(guess == 20)
#     print(guess != 20)
#     print(type(guess))
#     while counter < 5:
#         if guess != magic_number:
#             counter += 1
#             input("Unlucky! Try again! ")
#         elif guess == magic_number:
#             print("Congratulations!")
#             break
#
# guess()

# I need to check if this input matches a magic_number



# I need to let the user know if the response was write or not
#self five