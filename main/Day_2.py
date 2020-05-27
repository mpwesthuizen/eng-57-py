# using and managing strings
# single_quotes = 'Look! These are single quotes'
# print(single_quotes)
#
# double_quotes = "Look! These are single quotes"
# print(double_quotes)

# str_fix = 'I said \'Wow!\''
#
# quote_in_quote = 'I said "Wow!"'
# print(str_fix)
# print(quote_in_quote)

# # Slicing strings
#
# hw = "hello world "
# print(hw[0:5])
# print(len(hw))

# # strip
# white_space = "lots of space at the end           "
# print(len(white_space))
# print(len(white_space.strip()))

## some more methods

# using methods on substrings
#example = "some text here, we text with texting devices but can you see the subtext of the situation"
# print(example.count("text"))
# this counts how many times text appears.

# Bring everything to?
# print(example.lower())
# this changes all characters to lower case.

# print(example.upper())
# upper case too.

#print(example.capitalize())
# this method only capitalises the first character.

#print(example.replace("some", "plenty"))
# this method replaces the string with different characters. Note this is case sensitive.

# concatenation & casting
# concatenation is adding two strings together.
# casting is setting a variable's datatype.

# execute = 2
# y = 5.4
# z = "there's now a number 25.4 we put a space in!"
#
# print(str(execute) + str(y) +" "+ z)

# execute = "8"
# print(type(execute))
#
# execute = int(execute)
# print(execute)
# print(type(execute))
#
# execute = float(execute)
# print(execute)
# print(type(execute))
#
# execute = str(execute)
# print(execute)
# print(type(execute))
#
# execute = bool(execute)
# print(execute)
# print(type(execute))

# booleans and operators
# a = True
# b = False
# c = 2
# d = 1
#
# print(c == d)
# print(c != d)
# print(c >= d)
# print(c <= d)

# methods with booleans
# greetings = "Hello World!"
#
# print(greetings.startswith("H"))
# print(greetings.endswith("!"))

# # None as a datatype
# print(bool(None))
# print(bool(" "))
# # usins the bool shows how an empty string is still considered something where none is nothing.

# List

# list are exactly what you expect. They are lists.
# they are organised  with index. This means it starts with 0.

# example

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
# refactored_list.pop(3)
# print(refactored_list)
#
# # list.pop(index = -1)

# if statements
#


