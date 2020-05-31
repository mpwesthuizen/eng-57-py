# if_div
def if_div(num1, num2):
    return num1 % num2 == 0


# 3 % 3 check
def check_if_div33():
    var = 3 % 3 == 0
    return var == if_div(3, 3)

# 4 % 3 check
def check_if_div43():
    var = 4 % 3 == 0
    return var == if_div(4, 3)

# 5 % 5 check
def check_if_div55():
    var = 5 % 5 == 0
    return var == if_div(5, 5)

# 6 % 5 check
def check_if_div65():
    var = 6 % 5 == 0
    return var == if_div(6, 5)

# 15 % 3 check
def check_if_div153():
    var = 15 % 3 == 0
    return var == if_div(15, 3)

# 15 % 5 check
def check_if_div155():
    var = 15 % 5 == 0
    return var == if_div(15, 5)

#if __name__ = '__main__':
#    print('I was called directly')
# __name__ is a special feature in python that allows us to track where files are called from
# When called directly, therefore NOT imported, __name__ = __main__ when called from an import.