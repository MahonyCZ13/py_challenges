### Chapter 2 Challenge ###
'''
Check, if the number is even and multiple of 4.
'''
USER_NUMBER = int(input('Give me a number: '))

if USER_NUMBER % 4 == 0:
    print('The number is even and is multiple of 4.')
elif USER_NUMBER % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd')

### Extras ###

NUM = int(input('Give me a first number: '))
CHECK = int(input('Give me a second number: '))

if NUM % CHECK == 0:
    print('%s divides evenly by %s.' % (NUM, CHECK))
else:
    print('The numbers you have provided don\'t return even result.')
