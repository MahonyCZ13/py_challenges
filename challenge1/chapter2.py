### Chapter 2 Challenge ###

user_number = int(input('Give me a number: '))

if(user_number % 4 == 0):
    print('The number is even and is multiple of 4.')
elif(user_number % 2 == 0):
    print('The number is even.')
else:
    print('The number is odd')

### Extras ###

num = int(input('Give me a first number: '))
check = int(input('Give me a second number: '))

if(check % num == 0):
    print('The number %s divides evenly into %s.' % (check, num))
else:
    print('The numbers you have provided don\'t return even result.')
