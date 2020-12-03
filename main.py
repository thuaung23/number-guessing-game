# This program will answer if a number a user guesses is the same as a program's.
# Written by: Thu Aung.
# Written on: Sept 9, 2020.

print('Hello, welcome to the Number Guessing Game!')
print('I will be guessing a number between 1 and 100')
print('If your guess is within 10 of my number, I will say \'WARM\'.')
print('If you guess is more than 10 from my number, I will say \'COLD\'.')
print('If your next guess is closer than previous guess to my number, I will say \'WARMER\'.')
print('If your next guess is farther away than your previous guess to my number, I will say \'COLDER\'.')
print('Let\'s play the game!!!')

import random
num = random.randint(1,100)

# Used 0 as a place holder for comparing current guess and previous one
guesses = [0]

while True:

    # Get the number form user input.
    guess = int(input('Please enter the number you think is correct: '))

    # This is to make sure user enter a number between 1 and 100.
    if guess < 1 or guess >100:
        print('Your number is out of bound. Please enter a number between 1 and 100: ')
        continue

    # Add the current guess to list of previous guesses.
    guesses.append(guess)

    if guess == num:
        print(f'Congratulations! You\'ve got the correct number in just {len(guesses)} attempts.')
        break

    # For the first guess, guesses[-2] = 0 so it was evaluated as False and went down to next (else) section.
    # For the first guess, guesses = [0, guess]--> guesses[-2] = 0
    if guesses[-2]:

        # This is to compare whether the current or previous guess is closer to the correct number.
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    # Check the first guess whether it is close to the correct number.
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')