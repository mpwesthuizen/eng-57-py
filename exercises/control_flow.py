import time

# control flow

# control flow dictates where the code will run much like the damns in real life.

# in coding we do this with if statements and while loops we're going to look at if statements.

# if statements
# if statements work with booleans (true or false)
# we usually use comparison operators to equate and compare objects, adn result in True or False (Booleans)
# in python, block is defined by indentation


# Syntax if statements
# if <condition>:
#   block of code
# elif <condition>:
#   block of code
# else <optional_condition>:
#   block of code
# Note: when using multiple conditions put the tightest condtions first as the pointer stops at the first instance of conditions being satisfied therefore the tightest conditions can be overlooked otherwise, as earlier conditons are met first and the ponter stops before rechint the tightest condion.

# logical and
# syntax
# <condition> and <condition>
# both sides need to result in true to be true

# logical or
# syntax
# <condition> or <condition>
# one side needs to result in true to be true


# weather = input("What is the weather today? ")
# safety_alert = input("Is the safety alert is green, amber or red? ")
#
# if weather == "rainy":
#     time.sleep(2)
#     print("bring umbrella")
#
# elif weather == "stormy" and safety_alert == "red":
#     print("duck for cover")
#
# elif weather == "stormy":
#     print("Stay inside and watch the storm")
# else:
#     print("enjoy the sun")

# # FIZZBUZZ ALGO: AKA BIZZ,ZZUU
# execute = ""
# while True:
#
#         execute = input("Select a number (integer) greater than 5 \n type 'exit' to exit ")
#         if execute == "exit".lower():
#             break
#         execute = int(execute)
#
#         if execute%3 == 0 and execute%5 == 0:
#             print("\nBIZZZZU\n")
#
#         elif execute%5 == 0:
#             print("\nBIZZ\n")
#
#         elif execute%3 == 0:
#             print("\nZZUU\n")
#
#         elif execute <= 5:
#             print("\nWrong, the number needs to over 5 \n")
#
#         else:
#             print("\nSelect a better number. This one is not BIZZUU material.\n")

# FUNCTIONAL FIZZBUZZ SORTING ALGO:

def fizzbuzz(num1, num2):
    for item in range(1,int(num)+1):
        if item % (3*5) == 0:
            print("FIZZBUZZ")

        elif item % 3 == 0:
            print("FIZZ")

        elif item % 5 == 0:
            print("BUZZ")

        else:
             print(item)

start = input("Do you want to play BIZZZZUU? y/n ")

while True:
    if start.lower() == "n":
        print("Goodbye!")
        break

    elif start.lower() == "y":
        number = input("Enter your number ")
        if number == "penpineapplepen":
            break

    fizz = ("Choose your fizz ")
    buzz = ("Choose your  ")
    fizzbuzz(fizz, buzz)

# 2h20m