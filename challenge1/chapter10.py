### Chapter 10 Challenge ###
'''
Compares two lists for the same values.
'''
import random

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set(A) & set(B))

### Extras ###

# Generate two lists and compare them

C = random.sample(range(1, 50), 15)
D = random.sample(range(1, 50), 15)

# Another way of solving this without sets
RESULT = [i for i in C if i in D]

print(RESULT)

### Quicker example ###

# No quicker examples for this challenge
