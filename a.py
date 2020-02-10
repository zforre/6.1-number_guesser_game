#The computer will generate a random number between 1 to 100, 
# and the user has to guess it in 10 attempts.

import random

number_of_guesses = 0

print('Hey, what is your name?')
name = input()

number = random.randint(1,100)
print('Okay,',name ,'the number I am think of is between 1 and 100.')

while number_of_guesses < 10:
    print('Try and guess what number I am thinking of.')
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1
    if guess == number:
        break

if guess == number:
    # number_of_guesses = str(number_of_guesses)
    print('Okay,',name ,'you are correct! You must have read my mind')

if guess != number:
    print('Okay,',name ,'you were wrong and you are out of guesses.')

