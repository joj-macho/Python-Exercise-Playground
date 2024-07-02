'''
Exercise: Accessing and Slicing String Elements

This script demonstrates how to access and slice elements within strings.

Usage:
    Call the main function to see various examples of accessing and slicing
    strings.

Tags: strings, indexing, slicing, basics
'''


def main():
    '''Demonstrates accessing and slicing string elements.'''
    my_string = 'Hello, World!'
    print(f'First character: {my_string[0]}')
    print(f'Last character: {my_string[-1]}')
    print(f'Substring (0-5): {my_string[0:5]}')
    print(f'Substring (7-12): {my_string[7:12]}')


if __name__ == '__main__':
    main()
