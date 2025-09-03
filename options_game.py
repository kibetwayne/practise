#!The := operator, also known as the "walrus operator," allows you to assign a value to a variable as part of an expression
'''INSTEAD OF
            name = input("Hey, what's your name? ")
            if name:
    WRITE THIS INSTEAD
            if name := input('hey, what\'s your name? '):
'''


if name := input('hey, what\'s your name? '):
    should_we_play = input(f'hello {name}, ready to play? (yes|no): ').lower()
    play = should_we_play in ['yes', 'y']  # Checks if input is 'yes' or 'y'

    if play :
        direction = input('choose direction (left|right): ').lower()

        if direction == 'left':
            print('you fell off a cliff and died')

        elif direction == 'right':
            choice = input('you meet a bridge, do you swim of cross it(swim|cross): ').lower()

            if choice == 'swim':
                print('you got eaten by an crocodile and died')

            elif choice == 'cross':
                print('you won the game')

            else:
                print('invalid choice')

        else :
            print('invalid direction')

    else:
        print('Alright, maybe next time!n')

else:
    print('you didn\'t enter your name')
    
    