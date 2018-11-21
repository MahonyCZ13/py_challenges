### Chapter 4 Challenge ###
'''
Inputed value from user is chaked for even divisors.
'''
# Create list

NUM = int(input('Give me a number: '))

A = range(1, 100)

DIV_LIST = []

for i in A:
    if i % NUM == 0:
        DIV_LIST.append(i)

print(DIV_LIST)

### Extras ###

# No extras for this challenge
