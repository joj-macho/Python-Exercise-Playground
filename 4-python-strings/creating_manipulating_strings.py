'''
Exercise: Creating and Manipulating Strings

This script demonstrates how to create and modify strings.

Usage:
    Call the main function to see various examples of creating and
    manipulating strings.

Tags: strings, manipulation, basics
'''


def main():
    '''Demonstrates creating and manipulating strings.'''
    my_string = 'Hello, World!'
    print(f'Original string: {my_string}')

    upper_string = my_string.upper()
    print(f'Uppercase string: {upper_string}')

    replaced_string = my_string.replace('World', 'Python')
    print(f'Replaced string: {replaced_string}')


if __name__ == '__main__':
    main()
