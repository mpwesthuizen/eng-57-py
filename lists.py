# List

# list are exactly what you expect. They are lists.
# they are organised  with index. This means it starts with 0.

# example

refactored_list = ['Giggs', 'Mohamed', 'Betty']
#             index = [   0   ,    1    ,    3  ]

# print all of the list
print(refactored_list)

# access on entry of the list
# use the index with the list

print(refactored_list[2])

# accessing the first or the last index
print(refactored_list[0])
print(refactored_list[-1])

# Re-asseessing an entry
refactored_list[-2] = "Patrick"
print(refactored_list)
refactored_list[-1] = "Hotel of mom and dad"
print(refactored_list)

# Popping
# pop removes from an index and .remove("string") removes the first instance of the string in the list.
# removes last  entry from a list
refactored_list.pop()
print(refactored_list)

# add entry of mom and dad to end of list
refactored_list.append("Hotel of mom and dad")
print(refactored_list)

# refactoring
# this is the edit of code bases over iterations. In pycharm we can rename with shift + f6
# my_cringy_list is now refactored_list.

# remove entry and index 3
refactored_list.pop(3)
print(refactored_list)

# list.pop(index = -1)


