# List and collection
# list work as we expect them, they keep stuff in a list

# define a list using []
cring_land_l = []

# how lists are organized
# organised with index
# numbers that start at 0

# how to define a list
cring_land_l = ['Frank', 'Teresa', 'Allan', 'George']
# index        [   0  ]  [   1   ] [  2   ]  [   3  ]

# get one item from list
print(cring_land_l[0])

# get all item from list
print(cring_land_l)

# re assign item index 2 on list
cring_land_l[2] = 'Zack'
print(cring_land_l)

# add one item to list
# .append()
cring_land_l.append('Jo')
print(cring_land_l)

# add item in specific location on list
# .insert()
cring_land_l.insert(1, 'Kevin')
print(cring_land_l)