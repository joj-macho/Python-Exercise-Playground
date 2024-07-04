'''
Exercise: Fraction Calculator

This script performs basic mathematical operations on fractions.

Usage:
    Call the main function and follow the prompts.

Tags: fractions module, fractions, arithmetic operations
'''

from fractions import Fraction


def main():
    '''Demonstrates basic operations on fractions.'''
    frac1 = Fraction(input('Enter the first fraction (e.g., 1/2): '))
    frac2 = Fraction(input('Enter the second fraction (e.g., 3/4): '))

    print(f'Sum: {frac1 + frac2}')
    print(f'Difference: {frac1 - frac2}')
    print(f'Product: {frac1 * frac2}')
    print(f'Quotient: {frac1 / frac2}')


if __name__ == '__main__':
    main()
