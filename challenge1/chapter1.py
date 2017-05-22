### Chapter 1 Challenge ###
import datetime

# Getting user input
name = input('What is your name?: ')
age = int(input('Tell me your age: '))

#Get Date and Year
get_date = datetime.datetime.now()
current_year = get_date.year

# Calculate result
result = (current_year - age) + 100

# Compile message to user
msg = 'Hello there %s, you will reach 100 years in %s \n' % (name, result)

# Print it to user
print(msg)

### Extras ###

# Print the message x times based on user input and on the new line
userInput = input('How many times you want me to print above message?: ')

multi = int(userInput)

print(msg * multi)