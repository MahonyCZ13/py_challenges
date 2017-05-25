### Chapter 3 Challenge ###
'''
Lists numbers less than inputed value.
'''
A = [11, 21, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 5, 4, 2]

B = []

for i in A:
    if i < 5:
        B.append(i)

print(sorted(B))

### Extras ###

NUM = int(input('I will list numbers less than: '))
C = [i for i in A if i < NUM]
print(C)
