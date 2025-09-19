import random
print('Welcome to tht Number Guessing Game')
print("I'm thinking of a number between 1 and 100")

comp_guess = random.randint(1,100)
difficulty = input("Choose your difficulty. type 'easy' or 'hard': ").lower()
attempts = 0

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print(' invalid choice')
    
counter = attempts
correct_guess = False

while counter  > 0 and not correct_guess:
    print(f'you have {counter} attempts remaining to guess the number')
    my_guess = int(input('make a guess\n'))
    counter -= 1
    
    if my_guess > comp_guess and counter > 0:
        print('too high\nGuess again 💥')
    elif my_guess < comp_guess and counter > 0:
        print('too low\nGuess again 💥')
    elif my_guess == comp_guess:
        print(f'you got it the answer was {my_guess }🥳')
        correct_guess = True
    elif counter <= 0:
        print(f'you are out of attempts. game over 😭') 
         

