# The user will generate a random number between 1 to 100, and the computer 
# has to guess it in 10 attempts. The user will inform the computer 
# if the guess is too high or too low each time, and the computer will use 
# that information to inform its next guess.

import random

number_of_guesses = 0

print('Hey pick a number between 1 and 100 and I will try and guess it.')
number = input()

guess = random.randint(1,100)
# guess = int(guess)

while number_of_guesses < 10:
    print('Is it',guess,'?')
    number_of_guesses = number_of_guesses + 1
    if guess > number:
        guess -= 1
        guess = randint(1, guess)
    if guess < number:
        guess += 1
        guess = randint(guess, 100)
    if guess == number:
        break

if guess == number:
    print('I figured it out, it is',number,'! A computer read your mind.')

if number_of_guesses == 10:
    print('Oh well, I guess I cannot read minds afterall.')
