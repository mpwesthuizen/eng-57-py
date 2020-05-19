from datetime import date


# Define the following variables
# name, last_name, age, eye_color, hair_color

# name = 'James'
# last_name = 'Bond'
# eye_color = 'Blue'
# hair_color = 'Black'
# age = '30'

# Prompt user for input and Re-assign these
# name = input('What is your name? ')
# last_name = input('And your last name? ')
# eye_color = input('What is your eye colour? ')
# hair_color = input('What is your hair colour? ')
# age = input('And finally what is your age? ')
# convo = 'Hi {}! '.format(name) + 'Welcome, your age is {} '.format(age) + \
#         'you eyes are {} '.format(eye_color) + \
#         'and your hair color is {}. '.format(hair_color)
# print(convo)

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

# Section 2 - Calculate in what year was the person born? and responded back.
# print something like: 'You said you we're 28 hence you were born in 1991!'
age = input('How old are you? ')

def age_calc(x):
    today = date.today()
    return today.year() - x

age_calc(age)

dob = input('You said you are {} ').format(age) + 'hence your date of birth is {} '.format(age_calc)

# old_time = datetime.datetime.now()
# #print(old_time)
# new_time = old_time - datetime.timedelta(hours=2, minutes=10)
# print(new_time)


#Extra - Cast your input
#


