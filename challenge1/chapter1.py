### Chapter 1 Challenge ###
'''
Tells the user, in what year he or she will reach 100 years.
'''
import datetime

# Getting user input
NAME = input('What is your name?: ')
AGE = int(input('Tell me your age: '))

#Get Date and Year
GET_DATE = datetime.datetime.now()
CURRENT_YEAR = GET_DATE.year

# Calculate result
RESULT = (CURRENT_YEAR - AGE) + 100

# Compile message to user
MSG = 'Hello there %s, you will reach 100 years in %s \n' % (NAME, RESULT)

# Print it to user
print(MSG)

### Extras ###

# Print the message x times based on user input and on the new line
USER_INPUT = input('How many times you want me to print above message?: ')

MULTI = int(USER_INPUT)

print(MSG * MULTI)
