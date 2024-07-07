'''
Exercise: Sum of Even Numbers

This script calculates the sum of all even numbers up to a given number
using a for loop.

Usage:
    Call the function with the upper limit.

Tags: for loop, arithmetic operations, even numbers
'''


def main():
    '''Calculate the sum of all even numbers up to a given number.'''
    limit = int(input('Enter the upper limit: '))
    print(f'The sum of all even numbers up to {limit} is '
          f'{calculate_sum_even(limit)}')


def calculate_sum_even(limit):
    '''
    Calculates the sum of all even numbers up to a given number.

    Parameters:
        limit (int): The upper limit for the even numbers to sum.

    Returns:
        int: The sum of all even numbers up to the given limit.
    '''
    total = 0
    for i in range(2, limit + 1, 2):
        total += i
    return total


if __name__ == '__main__':
    main()
