'''
Exercise: Using Finally for Cleanup Actions

This script demonstrates how to use the finally block for cleanup actions.

Usage:
    Call the main function to see various examples of using the finally block.

Tags: exceptions, cleanup, basics
'''


def main():
    '''Demonstrates using finally for cleanup actions.'''
    try:
        file = open('example.txt', 'r')
        content = file.read()
    except FileNotFoundError:
        print('Error: File not found')
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print('File closed')


if __name__ == '__main__':
    main()
