'''
Exercise: Handling Exceptions

This script demonstrates how to handle exceptions using try-except blocks.

Usage:
    Call the main function to see various examples of handling exceptions.

Tags: exceptions, error handling, basics
'''


def main():
    '''Demonstrates handling exceptions.'''
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print('Error: Division by zero')

    try:
        with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print('Error: File not found')


if __name__ == '__main__':
    main()
