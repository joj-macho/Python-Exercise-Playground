'''
Exercise: Converting Integers to Other Number Bases

This script converts integers to binary, octal, and hexadecimal numbers.

Usage:
    Call the main function.

Tags: number conversion, bin(), oct(), hex()
'''


def main():
    '''Convert integers to binary, octal, and hexadecimal.'''
    number = int(input('Enter an integer: '))

    print(f'Binary: {bin(number)}')
    print(f'Octal: {oct(number)}')
    print(f'Hexadecimal: {hex(number)}')


if __name__ == '__main__':
    main()
