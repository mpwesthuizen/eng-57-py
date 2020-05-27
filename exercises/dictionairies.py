# # Dictonaries
#
# # definition and syntax
#
# # a dictionary is a data structure, like a list, but organized with keys and not indexes.
#
# # They are organized with 'key': 'value' pairs.
#
# # for example 'zebra': 'an African wild animal that looks like a horse but has stripes body'
#
# #  This means you can search data using keys, rather than index.
#
#
#
# # syntax
#
# # {}
#
# # my_dictionary = {
#
# # 'key': 'value',
#
# # 'key2': 'values',
#
# # }
#
# # print(type(my_dictionary))
#
#
#
# # Defining a dictionary
#
# # looking at our stingy landlords we need more info.. like they house they have and contact details.
#
#
#
# stingy_landlord1_dict = {
#
#     'name': 'Alfredo',
#
#     'phone_number': '0783271192',
#
#     'property': 'Birmingham, near Star City'
#
# }
#
#
#
# # printing dictionary
#
# print(stingy_landlord1_dict)
#
# print(type(stingy_landlord1_dict))
#
#
#
# # getting one value out
#
# print(stingy_landlord1_dict['name'])
#
# print(stingy_landlord1_dict['phone_number'])
#
#
#
#
#
# # re-assigning one value
#
# # list_example = ['hey', 1, 3, 5]
#
# # list_example[0] = 3456789
#
# stingy_landlord1_dict['name'] = "Alfredo de Medo"
#
# # print(stingy_landlord1_dict)
#
#
#
# # new key value pair
#
# stingy_landlord1_dict['address'] = "house 2, Unit 29 Watson Rd"
#
# # print(stingy_landlord1_dict)
#
#
#
# stingy_landlord1_dict['number_of_victims'] = 0
#
# # print(stingy_landlord1_dict)
#
# stingy_landlord1_dict['number_of_victims'] = stingy_landlord1_dict['number_of_victims'] + 1
#
# stingy_landlord1_dict['number_of_victims'] = stingy_landlord1_dict['number_of_victims'] + 1
#
# stingy_landlord1_dict['number_of_victims'] += 1
#
# print(stingy_landlord1_dict)
#
#
#
# # Get all the values out
#
#
#
#
#
# # special dictionary methods
#
# # (method are functions that belong to specific data type)
#
#
#
# # # .keys()
#
# print(stingy_landlord1_dict.keys())
#
# #
#
# # # .values()
#
# print(stingy_landlord1_dict.values())
#
#
#
# # .items()
#
# print(stingy_landlord1_dict.items())
#
#

# Dictionary basics exercise :D



#1 - Define a dictionary call story1, it should have the followign keys:

        # 'start', 'middle' and 'end'

story1 = {'start':'hi', 'middle':'die','end':'bye'}

#2 - Print the entire dictionary

print(story1)

#3 - Print the type of your dictionary

print(type(story1))

#4 - Print only the keys

print(story1.keys())

#4 - print only the values

print(story1.values())

#5 - print the individual values using the keys (individually, lots of printi commands)

print(story1['start'])
print(story1['middle'])
print(story1['end'])

#6 - Now let's add a new key:value pair.

story1['hero'] ='deadpool'
print(story1)
    # 'hero': yourSuperHero