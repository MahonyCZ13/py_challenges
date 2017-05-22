### Chapter 6 Challenge ###

string = input('Type a workd and I tell if it\'s palindrom or not: ')

# Create list for user inputed string
pali = []

# Create list for reversed string
rev_pali =[]

# Parse user inputed string into a list
for i in string:
    pali.append(i)

# Reverse order of the list
for i in reversed(pali):
    rev_pali.append(i)

# Join the reversed list into a string
string2 = ''.join(rev_pali)

# Compare user inputed string with reversed string
if(string == string2):
    print('This is a palindrom!: %s = %s' % (string, string2))
else:
    print('This is not a palindrom: %s != %s' % (string, string2))

### Extras ###

# No extras for this challenge

### Quicker example ###

string3 = input('Give me a another word: ')

string3 = str(string3)

rvs = string3[::-1]

print(rvs)

if (string3 == rvs):
    print('Palindrom!')
else:
    print('Not a palindrom...')