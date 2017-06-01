### Chapter 15 Challenge ###
'''
If user supplies a string this script will reverse its order.
'''

def string_reverse():
    '''(str) -> str

    Reverses word order inputed by user.

    >>> string_reverse('Hello there user')
    user there Hello
    >>> string('Are you alien?')
    ? alien you Are
    '''
    user = input('Give me a string and i will reverse it > ')
    result = str.split(user)
    print(result)
string_reverse()

### Extras ###

# No extras for this challenge

### Quicker example ###

# No quicker examples for this challenge
