'''
Exercise: While Loops

This script demonstrates how to use while loops for repeated execution as long
as a condition is true.

Usage:
    Call the main function to see various examples of while loops in action.

Tags: while loops, repetition, control flow
'''


def main():
    '''Demonstrates the use of while loops.'''
    count = 0
    while count < 5:
        print(f'Count: {count}')
        count += 1

    number = 10
    while number > 0:
        print(f'Number: {number}')
        number -= 2


if __name__ == '__main__':
    main()
