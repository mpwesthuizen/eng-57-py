import unititest
# Write a bizz and zzuu game ##project
# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)
# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'
# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu
# task
# https://trello.com/c/3x9BJdsY

# TESTING
# class TestingFizzbuzz(unititest.TestCase):
#     def test_div3
# unittest.main()
def check_digit_div_num(num):
    return num % 3 == 0


def check_if_div3(num):
    return num % 3 == 0

    # if num % 3 == 0:
    #     return True
    # else:
    #     return False

def check_if_div5(num):

    return num % 5 == 0

    # if num % 5 == 0:
    #     return True

    # else:
    #     return False

def fizz_buzz_print_check(num):
    if check_if_div5(num) and check_if_div3(num):
        print('it is divisible by 3 and 5')

    elif check_if_div5(num):  # only runs if the above if / elif statements were false
        print('yo it is div by 5')

    elif check_if_div3(num):
        print('yo it is div by 3')

    else:
        print(num)

while True:

        num = input('please give us a number to check if div by 3, 5 or 3 and 5?')

        if 'exit' in num:
            print('the force is with you...')

            break

        if num.isnumeric():
            num = int(num)

        for number in range(1, num + 1):
            fizz_buzz_print_check(number)

def check_if_digit_div_num(digit, num_div):

        if digit % num_div == 0:
            return True
        else:
            return False





def bizzbuzz(num1, num2, number):
    for digit in range(1, (int(number) + 1)):
        if check_if_digit_div_num(digit, num1) and check_if_digit_div_num(digit, num2):
            print('bizzzzuu')

        elif check_if_digit_div_num(digit, num2):
            print('zzuu')

        elif check_if_digit_div_num(digit, num1):
            print('bizz')
        else:
            print(digit)

#
# start = input('Are you ready to play BIZZBUZZ? (Y/N) ')
# while True:
#     if start.upper() == 'N':
#         print('Maybe next time...')
#         break
# #
#     elif start.upper() == 'Y':
#         number = input('Please enter number: ')
#         if number == 'penpinapplespen':
#             break
#         bizz = int(input('Choose your BIZZ: '))
#         buzz = int(input('Choose your ZZUU: '))
#         bizzbuzz(bizz, buzz, number)
#
#     else:
#         print("It's a Yes or No question.")
#         start = input('Are you ready to play BIZZBUZZ? >>(Y/N)<< '