'''
Exercise: ASCII Characters

This script displays the ASCII number and its corresponding text character
from 32 to 126.

Usage:
    Run the main function to see the ASCII character of a number.

Tags: ascii characters, chr(), print()
'''


def main():
    '''Displays ASCII character of a number.'''
    number = 126
    print(f'{number}: {chr(number)}')


if __name__ == '__main__':
    main()
