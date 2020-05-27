# List

# list are exactly what you expect. They are lists.
# they are organised  with index. This means it starts with 0.
#
# # example
#
# refactored_list = ['Giggs', 'Mohamed', 'Betty']
# #             index = [   0   ,    1    ,    3  ]
#
# # print all of the list
# print(refactored_list)
#
# # access on entry of the list
# # use the index with the list
#
# print(refactored_list[2])
#
# # accessing the first or the last index
# print(refactored_list[0])
# print(refactored_list[-1])
#
# # Re-asseessing an entry
# refactored_list[-2] = "Patrick"
# print(refactored_list)
# refactored_list[-1] = "Hotel of mom and dad"
# print(refactored_list)
#
# # Popping
# # pop removes from an index and .remove("string") removes the first instance of the string in the list.
# # removes last  entry from a list
# refactored_list.pop()
# print(refactored_list)
#
# # add entry of mom and dad to end of list
# refactored_list.append("Hotel of mom and dad")
# print(refactored_list)
#
# # refactoring
# # this is the edit of code bases over iterations. In pycharm we can rename with shift + f6
# # my_cringy_list is now refactored_list.
#
# # remove entry and index 3
# refactored_list.pop(2)
# print(refactored_list)

# list.pop(index = -1)


# Lists!



# Fine a list with cool things inside!

    # Examples: Christmas list, things you would by with the lottery

    # It must have 5 items

    # Complete the sentence:

    # Lists are organized using: _______????? indexes



example_xmas = ['walkie talkies', 'socks', 'lynx']



# Print the lists and check it's type

print(example_xmas)
print(type(example_xmas))




# Print the list's first object

print(example_xmas[0])



# Print the list's second object

print(example_xmas[1])



# Print the list's last object


print(example_xmas[2])


# Re-define the first item on the list and

example_xmas[example_xmas.index('walkie talkies')] = 'laptop'
print(example_xmas)

# Re-define another item on the list and print all the list

example_xmas[example_xmas.index('socks')] = 't-shirt'
print(example_xmas)




# Add an item to the list and print the list

example_xmas.append('watch')
print(example_xmas)


# Remove an item from the list and print the list

example_xmas.pop(example_xmas.index('lynx'))
print(example_xmas)


# Add two items to list and print the list

example_xmas.append('iphone')

example_xmas.append('money for icecream')

print(example_xmas)