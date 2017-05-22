### Chapter 3 Challenge ###

a = [11, 21, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 5, 4, 2]

a2 = []

for i in a:
    if i < 5:
        a2.append(i)

print(sorted(a2))

### Extras ###

num = int(input('I will list numbers less than: '))
a3 = [i for i in a if i < num]
print(a3)