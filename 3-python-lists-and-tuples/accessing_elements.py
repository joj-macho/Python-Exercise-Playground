'''
Exercise: Accessing Elements

This script demonstrates how to access elements in lists and tuples.

Usage:
    Call the main function to see various examples of accessing elements.

Tags: lists, tuples, indexing, slicing
'''


def main():
    '''Demonstrates accessing elements in lists and tuples.'''
    my_list = [1, 2, 3, 4, 5]
    print(f'First element of list: {my_list[0]}')
    print(f'Last element of list: {my_list[-1]}')
    print(f'Slice of list: {my_list[1:3]}')

    my_tuple = (1, 2, 3, 4, 5)
    print(f'First element of tuple: {my_tuple[0]}')
    print(f'Last element of tuple: {my_tuple[-1]}')
    print(f'Slice of tuple: {my_tuple[1:3]}')


if __name__ == '__main__':
    main()
