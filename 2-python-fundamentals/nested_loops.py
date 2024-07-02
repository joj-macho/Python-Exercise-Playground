'''
Exercise: Nested Loops

This script demonstrates how to use nested loops for more complex iterations.

Usage:
    Call the main function to see various examples of nested loops in action.

Tags: nested loops, iteration, control flow
'''


def main():
    '''Demonstrates the use of nested loops.'''
    for i in range(3):
        for j in range(2):
            print(f'i: {i}, j: {j}')

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix:
        for element in row:
            print(f'Element: {element}')


if __name__ == '__main__':
    main()
