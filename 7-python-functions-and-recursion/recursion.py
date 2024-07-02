'''
Exercise: Recursion and Recursive Functions

This script demonstrates how to write recursive functions and understand
the concept of recursion.

Usage:
    Call the main function to see various examples of recursion.

Tags: functions, recursion, basics
'''


def main():
    '''Demonstrates recursion and recursive functions.'''
    result = factorial(5)
    print(f'Factorial of 5: {result}')


def factorial(n):
    '''Returns the factorial of a number using recursion.'''
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    main()
