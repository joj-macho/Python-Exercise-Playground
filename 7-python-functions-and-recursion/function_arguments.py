'''
Exercise: Function Arguments and Return Values

This script demonstrates how to work with function arguments and return values.

Usage:
    Call the main function to see various examples of function arguments and
    return values.

Tags: functions, arguments, return values, basics
'''


def main():
    '''Demonstrates function arguments and return values.'''
    result = add(4, 2)
    print(f'Sum: {result}')


def add(a, b):
    '''Returns the sum of two numbers.'''
    return a + b


if __name__ == '__main__':
    main()
