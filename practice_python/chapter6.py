### Chapter 6 Challenge ###
'''
Check the user inputed string for palindrom.
'''

STRING = input('Type a word and I tell if it\'s palindrom or not: ')

# Create list for user inputed string
PALI = []

# Create list for reversed string
REV_PALI = []

# Parse user inputed string into a list
for i in STRING:
    PALI.append(i)

# Reverse order of the list
for i in reversed(PALI):
    REV_PALI.append(i)

# Join the reversed list into a string
STRING2 = ''.join(REV_PALI)

# Compare user inputed string with reversed string
if STRING == STRING2:
    print('This is a palindrom!: %s = %s' % (STRING, STRING2))
else:
    print('This is not a palindrom: %s != %s' % (STRING, STRING2))

### Extras ###

# No extras for this challenge

### Quicker example ###

STRING3 = input('Give me a another word: ')

STRING3 = str(STRING3)

RVS = STRING3[::-1]

print(RVS)

if STRING3 == RVS:
    print('Palindrom!')
else:
    print('Not a palindrom...')
