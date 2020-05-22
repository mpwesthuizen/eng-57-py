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
#     print("get naked")

# FIZZBUZZ ALGO: AKA BIZZ,ZZUU
x = ""
while x != 1:

        x = int(input("Select a number (integer) greater than 5 \n press 1 to exit "))
        if x%3 == 0 and x%5 == 0:
            print("BIZZZZU")

        elif x%5 == 0:
            print("BIZZ")

        elif x%3 == 0:
            print("ZZUU")

        else:
            "Select a better number"