### Chapter 13 Challenge ###
'''
To be added.
'''
def get_number():
    '''(int) -> int
    Gets useri input in form of int.
    '''
    num = int(input('Ho many Fibonacci numbers you want me to generate? > '))
    return num

def calculate(num):
    '''(int) -> int
    Generate Fibonacci sequence from inputed value.

    >>> calculate(3)
    1, 1, 2
    >>> calculate(7)
    1, 1, 2, 3, 5, 8, 13
    '''
    fib_list = []
    i = 1
    j = 0
    while i <= num:
        if(len(fib_list) == 0):
            result = j + 1
        else:
            result = fib_list[-1] + j
        fib_list.append(result)
        i += 1
        j += result
    print(fib_list)

calculate(get_number())
### Extras ###

# No extras for this challenge

### Quicker example ###

# No quicker examples for this challenge
