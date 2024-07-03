'''
Exercise: Swapping Two Numbers

This script swaps two numbers using a third variable.

Usage:
    Call the main function.

Tags: swapping, variables
'''


def main():
    '''Swap two numbers using a third variable.'''
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

    # Swapping
    temp = a
    a = b
    b = temp

    print(f'After swapping: a = {a}, b = {b}')


if __name__ == '__main__':
    main()
