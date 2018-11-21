##############################
# Challenge 2
##############################

mess = open("mess.txt", "r")

def letters(input):
    return ''.join(filter(str.isalpha, input))

c2 = letters(mess.read())

print (c2)