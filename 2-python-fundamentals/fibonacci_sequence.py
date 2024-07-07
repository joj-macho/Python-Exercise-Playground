'''
Exercise: Fibonacci Sequence

This script prints the Fibonacci sequence up to a given number of terms
using a while loop.

The Fibonacci sequence is a series of numbers where each number is the
sum of the two preceding ones, usually starting with 0 and 1.

Usage:
    Call the function with the number of terms.

Tags: while loop, Fibonacci sequence
'''


def main():
    '''Print the Fibonacci sequence up to a given number of terms.'''
    n_terms = int(input('Enter the number of terms: '))
    print_fibonacci(n_terms)


def print_fibonacci(n_terms):
    '''
    Prints the Fibonacci sequence up to a given number of terms.

    Parameters:
        n_terms (int): The number of terms to print.

    Returns:
        None
    '''
    a, b = 0, 1
    count = 0
    while count < n_terms:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()


if __name__ == '__main__':
    main()
