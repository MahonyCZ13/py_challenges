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
    result = user.split()
    finish = []
    for i in reversed(result):
        finish.append(i)

    print(' '.join(finish))

string_reverse()

### Extras ###

# No extras for this challenge

### Quicker example ###

def reverse_word(word):
    '''(str) -> str

    Reverses word order inputed by user.

    >>> string_reverse('Hello there user')
    user there Hello
    >>> string('Are you alien?')
    ? alien you Are
    '''
    print(' '.join(word.split()[::-1]))

reverse_word('Hello there user')
