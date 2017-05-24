### Chapter 9 Challenge ###

import random

i = 1
running = True

while running:
    i += 1
    user  = input('Guess a number from 1 to 5! (or type \'q\' to quit): ')
    if(user == 'q'):
        print('You have played %s games.' % i)
        running = False
    else:
        user = int(user)
        gen = random.randint(1,5)

        if(user == gen):
            print('Yes!! It\'s a match! The computer thought %s and you guessed %s.' % (gen, user))
        else:
            print('Sadly, wrong. Computer thought %s and you guessed %s.' % (gen, user))


### Extras ###

# Count how many games user played. - Done
# Type 'q' to quit the game otherwise continue playing. - Done

### Quicker example ###

# No quicker examples for this challenge