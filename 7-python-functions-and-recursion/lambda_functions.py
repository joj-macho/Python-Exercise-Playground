'''
Exercise: Lambda Functions

This script demonstrates how to use lambda functions for short,
anonymous functions.

Usage:
    Call the main function to see various examples of lambda functions.

Tags: functions, lambda, basics
'''


def main():
    '''Demonstrates lambda functions.'''
    def square(x): return x ** 2
    print(f'Square of 5: {square(5)}')

    def add(a, b): return a + b
    print(f'Sum of 3 and 4: {add(3, 4)}')


if __name__ == '__main__':
    main()
