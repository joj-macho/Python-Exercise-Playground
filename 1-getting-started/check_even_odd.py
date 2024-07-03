'''
Exercise: Determining if a Number is Even or Odd

This script determines if a given number is even or odd.

Usage:
    Call the function with the number to check.

Tags: modulo operations, comparison operations, Boolean value
'''


def main():
    '''Main function to demonstrate even or odd check.'''
    number = 15
    print(f'Is the number, {number}, even? {is_even(number)}.')
    print(f'Is the number, {number}, odd? {is_odd(number)}.')


def is_even(number):
    '''
    Checks if a number is even.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    '''
    return number % 2 == 0


def is_odd(number):
    '''
    Checks if a number is odd.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    '''
    return number % 2 != 0


if __name__ == '__main__':
    main()
