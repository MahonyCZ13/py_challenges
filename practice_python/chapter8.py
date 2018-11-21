### Chapter 8 Challenge ###
'''
Rock, paper scissors game for two players.
'''

while True:
    USR_CMD = input('Type \'start\' to start the game or \'quit\' to end the game > ')
    if USR_CMD == 'quit':
        break
    elif USR_CMD == 'start':
        USER1 = int(input('Player 1: Rock paper or scissors?: '))
        USER2 = int(input('Player 2: Rock paper or scissors?: '))

        RESULT = [" ", "rock", "paper", "scissors"]

        if USER1 == USER2:
            print('It\'s a tie!')
        elif USER1 == 3 and USER2 == 1:
            print('Player 2 picked %s and won!' % RESULT[USER2])
        elif USER1 == 1 and USER2 == 2:
            print('Player 2 picked %s and won!' % RESULT[USER2])
        elif USER1 == 2 and USER2 == 3:
            print('Player 2 picked %s and won!' % RESULT[USER2])
        else:
            print('Player 1 picked %s and won!' % RESULT[USER1])
    else:
        print('This is a bad command.')

### Extras ###

# No extras for this challenge

### Quicker example ###

'''if(user1 == user2):
    print('It\'s a tie!')
elif((user1 == 3 and user2 == 1) or (user1 == 1 and user2 == 2) or (user1 == 2 and user2 == 3)):
    print('Player 2 picked %s and won!' % result[user2])
else:
    print('Player 1 picked %s and won!' % result[user1])'''