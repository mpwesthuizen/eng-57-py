import datetime

# # Practice strings
#
# # Welcome to Sparta - exercise
#
#
#
# # Version 1 specs - with concatenation
#
# # define a variable name, and assign a string
# var = str(10)
#
#
# # prompt the user for input and ask the user for his/her name
# name = input("What is your name? ")
# # re assign the original variable this this input
#
# var = name
#
#
# # use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
#
# welcome = "Welcome" + " " + var.strip().capitalize() + "!"
# welcome_2 = "Welcome {}!".format(var)
#
# print(welcome)
# # Version 2 - with interpolation
#
# welcome_2 = "Welcome {}!".format(var)
#
# # ask the user for a first name, save it in a variable
#
# first_q = input("Please give my your first name ")
#
# first_name = first_q
#
# # ask the user for a last name, save it in a variable
#
# last_q = input("Please give my your surname ")
#
# surname = last_q
#
# # use interpolation to print the message
#
# thanks = print(f"Thanks {first_name} {surname}")
#
#
# Calculate year of birth

# gather details on age and name
nme = input("Please give my your name ")
name = nme.capitalize()
age = int(input('How old are you? '))

current = datetime.datetime.now()
b_year = current - datetime.timedelta(days= 365.25 *age)
birth_year = b_year.year

print(f"Wow {name}, you are {age} years old so you were born in {birth_year}!")
# print something like

# OMG <person>, you are <age> years old so you were born in <year>