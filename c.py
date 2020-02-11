# The user will generate a random number between 1 to 100, and the computer 
# has to guess it in 10 attempts. The user will inform the computer 
# if the guess is too high or too low each time, and the computer will use 
# that information to inform its next guess.

import random

print('Hey pick a number between 1 and 100 and I will try and guess it.')
number = int(input('Your Number:'))

guess = random.randint(1,100)
counter = 0

while counter < 10:
    counter += 1

    # print('Is it',guess,'?')
    # number_of_guesses = number_of_guesses + 1
    # if guess > number:
    #     guess -= 1
    #     guess = randint(1, guess)
    # if guess < number:
    #     guess += 1
    #     guess = randint(guess, 100)

    # print(guess)
    # print(number)
    if guess == number:
        print('I figured it out, it is',number,'! A computer read your mind.')
        break
    elif guess < number:
        print('I guessed',guess,'that was too low!')
        guess += 1
        guess = random.randint(guess, 100)
    elif guess > number:
        print('I guessed',guess,'that was too high!')
        guess -= 1
        guess = random.randint(1, guess)

if counter == 10:
    print('Oh well, I guess I cannot read minds afterall.')
