'''
Exercise: Sum of the First n Positive Integers

This script calculates the sum of all n integers from 1 to n.

Formula:
    Sum = n * (n + 1) / 2
where:
    - n is the number of positive integers to sum.

Usage:
    Call the function with a positive integer n.

Tags: arithmetic operations, sum, positive integers
'''


def main():
    '''Main function to demonstrate sum of n positive integers.'''
    n = 100
    print(f'Sum of first {n} positive integers = {sum_of_n_integers(n)}')


def sum_of_n_integers(n):
    '''
    Calculates the sum of the first n positive integers.

    Parameters:
        n (int): The number of integers to sum.

    Returns:
        int: The sum of the first n positive integers
    '''
    return (n * (n + 1) // 2)


if __name__ == '__main__':
    main()
