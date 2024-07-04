'''
Exercise: Converting Decimals to Fractions

This script converts a decimal number to a fraction.

Usage:
    Call the main function and follow the prompts.

Tags: decimal conversion, fractions
'''

from fractions import Fraction


def main():
    '''Convert a decimal number to a fraction.'''
    decimal = float(input('Enter a decimal number: '))
    fraction = Fraction(decimal).limit_denominator()
    print(f'The fraction representation of {decimal} is {fraction}')


if __name__ == '__main__':
    main()
