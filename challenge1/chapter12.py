### Chapter 7 Challenge ###
'''
Takes list and create a new one of only first and a last elemets.
'''
def create_list():
    '''() -> list

    Creates list from a list from only the first and the last elements.

    >>> create_list()
    [1, 2, 3, 4] -> [1, 4]
    >>> create_list()
    [3, 1, 6, 3, 1] -> [3, 1]

    '''
    base_list = [5, 10, 15, 20, 25]
    new_list = []

    if len(base_list) < 2:
        print('The is not enough elements to work on...')
    else:
        new_list.insert(0, base_list.pop(0))
        new_list.append(base_list.pop())

        print('%s -> %s' % (base_list, new_list))

create_list()

### Extras ###

# No extras for this challenge

### Quicker example ###

A = [5, 10, 15, 20, 25]

def second_way(lst):
    '''
    Second way of the function creat_list()
    '''
    return [lst[0], lst[-1]]

print(second_way(A))
