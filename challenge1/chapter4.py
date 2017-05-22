### Chapter 4 Challenge ###

# Create list

num = int(input('Give me a number: '))

a = range(1, 100)

div_list = []

for i in a:
    if i % num == 0:
        div_list.append(i)

print(div_list)

### Extras ###

# No extras for this challenge