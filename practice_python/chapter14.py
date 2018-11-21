### Chapter 14 Challenge ###
'''
Takes a list with miltiple values a returns a list with these values minus the duplicates.
'''

def trim_list():
    '''(list) -> list

    Creates new list without the duplicates in the supplied list.

    >>> trim_list([1, 1, 2, 3, 4, 4, 5])
    [1, 2, 3, 4, 5]
    >>> trim_list([1, 2, 2])
    [1, 2]
    '''
    list_one = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 7]
    list_two = []

    i = 1

    while i <= len(list_one):
        if i in list_one:
            list_two.append(i)
        i += 1

    print(list_two)

trim_list()


### Extras ###

## Using sets

def trim_set():
    '''(set) -> set

    Same as trim_list but usig sets.
    '''
    set_one = set([1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 7])

    result = list(set(set_one))

    print(result)

trim_set()

### Quicker example ###

def trim_quick():
    '''(list) - > list
    Same as trim_list but usig 'not in' condition.
    '''
    list_three = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7]
    list_four = []

    for i in list_three:
        if i not in list_four:
            list_four.append(i)
    print(list_four)

trim_quick()
