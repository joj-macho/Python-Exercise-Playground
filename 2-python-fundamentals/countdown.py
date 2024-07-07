'''
Exercise: Countdown

This script performs a countdown from a given number to zero using a
while loop.

Usage:
    Call the function with the starting number.

Tags: while loop, countdown
'''


def main():
    '''Perform a countdown from a given number to zero.'''
    start = int(input('Enter the starting number: '))
    countdown(start)


def countdown(start):
    '''
    Performs a countdown from a given number to zero.

    Parameters:
        start (int): The starting number for the countdown.

    Returns:
        None
    '''
    while start >= 0:
        print(start)
        start -= 1


if __name__ == '__main__':
    main()
