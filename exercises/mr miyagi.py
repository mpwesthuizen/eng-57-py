# mr Miyagi trainee



# make a mr miyagi virtual assistant



# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

intro = input('???:Hi! I Mr Miyagi. What is your name? ')

# Ask for user input and depending on the response, mr Miyagi will respond.

#
name = print(f'Mr Miyagi: Ahh! so you {intro}son')

# prompt user for input
instruction = ""
while True:
    instruction = input('What do you want to do? ')

    if instruction == 'Sensei, I am at peace':
        print('Sometimes, what heart know, head forget')
        break

    elif instruction == '%?':
        print('questions are wise, but for now. Wax on, and Wax off!')

    elif instruction != 'Sensei,%':
        print('You are smart, but not wise - address me as Sensei please')

    elif instruction == '%block%' or instruction == '%blocking%':
        print('Remember, best block, not to be there...')

    else:
        print('do not lose focus. Wax on. Wax off.')

# Evaluate each input and print the appropriate responses

# Follow these rules:

#

# every time you ask a question --> Mr. Miyagi responde with

    # --> 'questions are wise, but for now. Wax on, and Wax off!'

# every statement/question must start with Sensei, otherwise:

    # --> 'You are smart, but not wise - address me as Sensei please'

# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with

    # --> 'Remember, best block, not to be there..'

# anything else you say:

    # --> 'do not lose focus. Wax on. Wax off.'





# Make it so you keep playing until we say: 'Sensei, I am at peace'

    # --> 'Sometimes, what heart know, head forget'



# your_response = input('(MR.Miyagi)... -.-')



#  EXTRA:

#  make it run continuously

#  consider best practices of functions - make this functional