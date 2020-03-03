# Lists!

# Find a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????
christmas_list = ['yacht', 'car', 'laptop', 'ps4', 'house']

# Print the lists and check it's type
print(type(christmas_list))

# Print the list's first object
print(christmas_list[0])

# Print the list's second object
print(christmas_list[1])

# Print the list's last object
print(christmas_list[4])

# Re-define the first item on the list and
christmas_list[0] = 'Bus'

# Re-define another item on the list and print all the list
christmas_list[2] = 'bike'
print(christmas_list)

# Add an item to the list and print the list
christmas_list.append('dog')
print(christmas_list)

# Remove an item from the list and print the list
christmas_list.remove('bike')
print(christmas_list)

# Add two items to list and print the list
christmas_list.append('shoes')
christmas_list.append('frog')
print(christmas_list)
