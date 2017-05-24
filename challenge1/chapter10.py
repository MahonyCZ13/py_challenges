### Chapter 10 Challenge ###

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set(a) & set(b))

### Extras ###

# Generate two lists and compare them

import random

c = random.sample(range(1, 50), 15)
d = random.sample(range(1, 50), 15)

# Another way of solving this without sets
result = [i for i in c if i in d]

print(result)

### Quicker example ###

# No quicker examples for this challenge