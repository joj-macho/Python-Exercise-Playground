'''
Exercise: Defining Functions

This script demonstrates how to define and use functions in Python.

Usage:
    Call the main function to see various examples of defining and using
    functions.

Tags: functions, basics
'''


def main():
    '''Demonstrates defining and using functions.'''
    greet('Alice')
    greet('Bob')


def greet(name):
    '''Prints a greeting message.'''
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
