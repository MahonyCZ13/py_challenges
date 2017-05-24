### Chapter 8 Challenge ###

while True:
    usr_cmd = input('Type \'start\' to start the game or \'quit\' to end the game > ')
    if(usr_cmd == 'quit'):
        break
    elif(usr_cmd == 'start'):
        user1 = int(input('Player 1: Rock paper or scissors?: '))
        user2 = int(input('Player 2: Rock paper or scissors?: '))
        # print('These are the inputs from Player 1: %s and Player 2: %s.' % (user1, user2))

        result = [" ", "rock", "paper", "scissors"]

        if(user1 == user2):
            print('It\'s a tie!')
        elif(user1 == 3 and user2 == 1):
            print('Player 2 picked %s and won!' % result[user2])
        elif(user1 == 1 and user2 == 2):
            print('Player 2 picked %s and won!' % result[user2])
        elif(user1 == 2 and user2 == 3):
            print('Player 2 picked %s and won!' % result[user2])
        else:
            print('Player 1 picked %s and won!' % result[user1])
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