### Chapter 11 Challenge ###

import math

def get_number():
    user_num = int(input('Give me a number > '))
    return user_num

def prime_checker(num):

    list_div = []
    i = 1
    
    while i <= (math.sqrt(num)):
        if(num % i == 0):
            list_div.append(i)
        i += 1
    
    if(len(list_div) == 1):
        print('This is a prime number!')
    else:
        print('This is not a prime number, because it has %s divisors.' % (len(list_div) * 2))
             
prime_checker(get_number())
    

### Extras ###

# No extras for this challenge

### Quicker example ###

num2 = int(input('Insert a number: '))

a = [x for x in range(2, num2) if num2 % x == 0]

def is_prime(n):
    if num2 > 1:
        if len(a) == 0:
            print('This prime number!')
        else:
            print('Not prime!')
    else:
        print('not prime!')

is_prime(num2)