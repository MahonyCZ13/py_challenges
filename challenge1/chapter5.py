### Chapter 5 Challenge ###
'''
Check the lists for the same values.
'''
import random

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# this method only works in equaly sized lits
RESULT = [i for i, j in zip(A, B) if i == j]
print(RESULT)

### Extras ###

C = random.sample(range(1, 100), 15)
D = random.sample(range(1, 100), 20)

print(set(C) & set(D))
