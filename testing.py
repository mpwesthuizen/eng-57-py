if __name__ = '__main__':
    print('I was called directly')
# __name__ is a special feature in python that allows us to track where files are called from
# When called directly, therefore NOT imported, __name__ = __main__ when called from an import.