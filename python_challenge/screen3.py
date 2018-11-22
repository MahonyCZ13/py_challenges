##############################
# Challenge 3
##############################

import re

body = open("bodyguards.txt", "r")

r = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', body.read())
m = ''.join(r)

if m is not None:
    print (m)