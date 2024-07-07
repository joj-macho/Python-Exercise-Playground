'''
Exercise: Guessing Game

This script implements a simple number guessing game using a while loop
and the break statement.

The program randomly selects a number between 1 and 100, and the user
tries to guess it. The game provides feedback if the guess is too high or
too low and continues until the user guesses the correct number.

Usage:
    Run the script and follow the prompts.

Tags: while loop, break, random module, number guessing game
'''

import random


def main():
    '''Play a number guessing game.'''
    target = random.randint(1, 100)
    print('Guess the number (between 1 and 100):')
    while True:
        guess = int(input('Enter your guess: '))
        if guess < target:
            print('Too low!')
        elif guess > target:
            print('Too high!')
        else:
            print('Congratulations! You guessed the correct number.')
            break


if __name__ == '__main__':
    main()
