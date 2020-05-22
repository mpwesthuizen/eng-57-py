# Dictionairies
# definitions
# a dictionary is a data structure, like a list, but organised with a key and not indexes

# They are organised with key: 'value' pairs
# for example 'zebra': "an african wild animal that looks like a horse but has stripes on its body."

# this means you can search data using keys, rather than index.

# syntax
my_dictionary ={'key':'value'}
print(type(my_dictionary))

# Defining a dictionary
# looking at our stringy landlords we need more info.. like the houses they have and contact detail.

stingy_dict = {
    'name': 'giggs',
    'phone_number' : '0745 678 910',
    'property_type': 'flat'
}

# printing dictionary
print(stingy_dict)
print(type(stingy_dict))

# getting one value out
print(stingy_dict['name'])
print(stingy_dict['phone_number'])

# re-assigning one value

stingy_dict['name'] = "alfredo de medo"
print(stingy_dict)

# new key value pair
stingy_dict['property_type'] = "house 2, Unit 29 Watson Rd"
print(stingy_dict)

stingy_dict['number_of_victims'] = 0
stingy_dict['number_of_victims'] += 1
print(stingy_dict)

# Get all the values out

# special dictionary methods
# (methods are functions that belong to specific data types)

# .keys()
print(stingy_dict.keys())

# .values()
print(stingy_dict.values())

# .items()
print(stingy_dict.items())
