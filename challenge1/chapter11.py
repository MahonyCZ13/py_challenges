### Chapter 11 Challenge ###
'''
Gets number from a user and check it, if it's a prime number.
'''
import math

def get_number():
    '''() -> number

    Return a number inputed from user.

    >>> get_number()
    Give me a number >
    '''

    user_num = int(input('Give me a number > '))

    return user_num

def prime_checker(num):
    '''(number) -> number

    Return result, if supplied number is a prime number.

    >>> prime_checker(2)
    This is a prime number!
    >>> prime_checker(24)
    This is not a prime number, because it has 8 divisors.
    '''

    list_div = []
    i = 1

    while i <= (math.sqrt(num)):
        if num % i == 0:
            list_div.append(i)
        i += 1

    if len(list_div) == 1:
        print('This is a prime number!')
    else:
        print('This is not a prime number, because it has %s divisors.' % (len(list_div) * 2))

prime_checker(get_number())

### Extras ###

# No extras for this challenge

### Quicker example ###

USER_INPUT = int(input('Insert a number: '))

A = [x for x in range(2, USER_INPUT) if USER_INPUT % x == 0]

def is_prime(num):
    '''(int) -> str

    Return result, if supplied number is a prime number

    >>> is_prime(2)
    This is a prime number!
    >>> is_prime(24)
    Not prime!
    '''

    if num > 1:
        if len(A) == 0:
            print('This is a prime number!')
        else:
            print('Not prime!')
    else:
        print('Not Prime!')

is_prime(USER_INPUT)
