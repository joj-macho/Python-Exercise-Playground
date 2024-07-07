'''
Exercise: Prime Numbers

This script prints all prime numbers up to a given limit using a for loop
and the continue statement.

A prime number is a natural number greater than 1 that is not divisible
by any number other than 1 and itself.

Usage:
    Call the function with the upper limit.

Tags: for loop, continue, prime numbers
'''


def main():
    '''Print all prime numbers up to a given limit.'''
    limit = int(input('Enter the upper limit: '))
    print(f'The prime numbers up to {limit} are:')
    print_primes(limit)


def print_primes(limit):
    '''
    Prints all prime numbers up to a given limit.

    Parameters:
        limit (int): The upper limit for the prime numbers.

    Returns:
        None
    '''
    for num in range(2, limit + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
    print()


if __name__ == '__main__':
    main()
