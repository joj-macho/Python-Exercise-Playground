'''
Exercise: Raising Exceptions

This script demonstrates how to raise exceptions in your code.

Usage:
    Call the main function to see various examples of raising exceptions.

Tags: exceptions, raising, basics
'''


def main():
    '''Demonstrates raising exceptions.'''
    def check_positive(number):
        if number < 0:
            raise ValueError('Number must be positive')

    try:
        check_positive(-5)
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
