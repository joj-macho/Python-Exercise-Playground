'''
Exercise: Number Guessing Game

This script implements a simple number guessing game where the user has to guess a randomly chosen number.

The program randomly selects a number between 1 and 100, and the user
tries to guess it. The game provides feedback if the guess is too high or
too low and continues until the user guesses the correct number.

Usage:
    Call the function to start the game.

Tags: while loop, umeric types, loops, user input, random module, number guessing game
'''

import random

def main():
    '''Play the simple number guessing game.'''
    number = random.randint(1, 100)
    print(number)
    for _ in range(10):  # Attempt limit is 10
        guess = int(input('Guess the number (1-100): '))
        if guess == number:
            print('Congratulations! You guessed the number.')
            return
        elif guess < number:
            print('Too low!')
        else:
            print('Too high!')
    print(f'Game Over! The correct number was {number}.')

if __name__ == '__main__':
    main()
