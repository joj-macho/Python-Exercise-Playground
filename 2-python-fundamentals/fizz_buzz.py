'''
Exercise: FizzBuzz

This script implements the FizzBuzz game.

The rules of FizzBuzz:
    - Print "Fizz" for numbers that are multiples of 3.
    - Print "Buzz" for numbers that are multiples of 5.
    - Print "FizzBuzz" for numbers that are multiples of both 3 and 5.
    - Print the number itself for all other numbers.

Usage:
    Call the function with the range of numbers.

Tags: for loop, if-elif-else, game, arithmetic operations
'''


def main():
    '''Execute the Fizz Buzz sequence.'''
    fizz_buzz()


def fizz_buzz():
    '''Prints the Fizz Buzz sequence from 1 to 100.'''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
