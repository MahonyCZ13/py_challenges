### Chapter 13 Challenge ###
'''
To be added.
'''

import sys

def get_number():
    '''(int) -> int
    Gets user input in form of int.
    '''
    try:
        num = int(input('How many Fibonacci numbers you want me to generate? > '))
        return num
    except ValueError:
        print('This is not a number!')
        sys.exit()


def calculate(num):
    '''(int) -> int
    Generate Fibonacci sequence from inputed value.

    >>> calculate(3)
    [1, 1, 2]
    >>> calculate(7)
    [1, 1, 2, 3, 5, 8, 13]
    '''
    fib_list = [0, 1]
    i = 0
    while i <= num:
        result = fib_list[-1] + fib_list[-2]
        fib_list.append(result)
        i += 1

    print(fib_list[:num])

calculate(get_number())
### Extras ###

# No extras for this challenge

### Quicker example ###

# No quicker examples for this challenge
