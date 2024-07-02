'''
Exercise: String Methods

This script demonstrates various methods available for string manipulation.

Usage:
    Call the main function to see various examples of string methods.

Tags: strings, methods, manipulation
'''


def main():
    '''Demonstrates various string methods.'''
    my_string = 'Hello, World!'
    print(f'Original string: {my_string}')

    upper_string = my_string.upper()
    print(f'Uppercase string: {upper_string}')

    lower_string = my_string.lower()
    print(f'Lowercase string: {lower_string}')

    split_string = my_string.split(',')
    print(f'Split string: {split_string}')

    stripped_string = my_string.strip('!')
    print(f'Stripped string: {stripped_string}')


if __name__ == '__main__':
    main()
