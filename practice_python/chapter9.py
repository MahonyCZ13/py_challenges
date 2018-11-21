### Chapter 9 Challenge ###
'''
Guesser game with a computer.
'''

import random

i = 1
RUNNING = True

while RUNNING:
    i += 1

    USER = input('Guess a number from 1 to 5! (or type \'q\' to quit): ')

    if USER == 'q':
        print('You have played %s games.' % i)
        RUNNING = False
    else:
        USER = int(USER)
        GEN = random.randint(1, 5)

        if USER == GEN:
            print('Yes!! It\'s a match! The computer thought %s and you guessed %s.' % (GEN, USER))
        else:
            print('Sadly, wrong. Computer thought %s and you guessed %s.' % (GEN, USER))


### Extras ###

# Count how many games user played. - Done
# Type 'q' to quit the game otherwise continue playing. - Done

### Quicker example ###

# No quicker examples for this challenge
