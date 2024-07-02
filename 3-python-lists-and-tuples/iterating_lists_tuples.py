'''
Exercise: Iterating Through Lists and Tuples

This script demonstrates how to iterate through lists and tuples.

Usage:
    Call the main function to see various examples of iterating through lists
    and tuples.

Tags: lists, tuples, iteration, data structures
'''


def main():
    '''Demonstrates iterating through lists and tuples.'''
    my_list = [1, 2, 3, 4, 5]
    print('Iterating through list:')
    for item in my_list:
        print(f'List item: {item}')

    my_tuple = (1, 2, 3, 4, 5)
    print('Iterating through tuple:')
    for item in my_tuple:
        print(f'Tuple item: {item}')


if __name__ == '__main__':
    main()
