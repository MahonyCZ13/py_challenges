### Chapter 4 Challenge ###

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# this method only works in equaly sized lits
result = [i for i, j in zip(a, b) if i ==j]
print(result)

### Extras ###

import random

c = random.sample(range(1, 100), 15)
d = random.sample(range(1, 100), 20)



print(set(c) & set(d))