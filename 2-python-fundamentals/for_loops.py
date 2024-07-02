'''
Exercise: For Loops

This script demonstrates how to use for loops to iterate over sequences.

Usage:
    Call the main function to see various examples of for loops in action.

Tags: for loops, iteration, sequences
'''


def main():
    '''Demonstrates the use of for loops.'''
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(f'Number: {number}')

    word = 'Python'
    for letter in word:
        print(f'Letter: {letter}')


if __name__ == '__main__':
    main()
