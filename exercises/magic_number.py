import random


# Magic number game!

# I want you to use operators

# equate something



# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
keep_playing = True

while keep_playing == True:



# We should define/assign number to a variable called magic_number

    magic_number = random.randint(1,5)



# I need to ask user for input

    guess = int(input("Numbers 1 - 5, What number am I thinking about? "))



# I need to check if this input matches a magic_number

    if guess == magic_number:
        correct = input("Amazing you correctly guessed the number with only 20% probabilty of accuracy, self five!\n Do want to continue? y/n")
        if correct == "y".lower():
            keep_playing = True
        else:
            keep_playing = False

    else:
        print("Better luck next time!")
# I need to let the user know if the response was write or not

#self five