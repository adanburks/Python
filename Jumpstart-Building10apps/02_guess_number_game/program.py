import random

print('---------------------------------------')
print('        GUESS THAT NUMBER GAME')
print('---------------------------------------')
print()

name = input('What is your name? ')
the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < -1:
        print('{}, you are supposed to pick a number greater than 0'.format(name))
    elif guess > 100:
        print('{}, you are supposed to pick a number less than 100'.format(name))
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too high! '.format(name, guess))
    elif guess < the_number:
        print('Sorry {}, your guess of {} is too low! '.format(name, guess))
    else:
        print('Congratulations {}, your guess of {} is correct!!!'.format(name, guess))

print('done!')

