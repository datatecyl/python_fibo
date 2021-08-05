def valid_code(nr):
    print('\nStarting validation process...')
    if nr > 0:
        print(nr, 'is valid.')
        return True
    else:
        print('The input number is invalid. Please give a number bigger than 0')
        return False