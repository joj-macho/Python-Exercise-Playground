'''
Exercise: List and Tuple Methods

This script demonstrates various methods available for lists and tuples.

Usage:
    Call the main function to see various examples of list and tuple methods.

Tags: lists, tuples, methods, data structures
'''


def main():
    '''Demonstrates various list and tuple methods.'''
    my_list = [1, 2, 3, 4, 5]
    print(f'Original list: {my_list}')
    my_list.append(6)
    print(f'List after append: {my_list}')
    my_list.remove(3)
    print(f'List after remove: {my_list}')
    my_list.reverse()
    print(f'List after reverse: {my_list}')
    my_list.sort()
    print(f'List after sort: {my_list}')

    my_tuple = (1, 2, 3, 4, 5)
    print(f'Tuple: {my_tuple}')
    print(f'Tuple count of 3: {my_tuple.count(3)}')
    print(f'Tuple index of 4: {my_tuple.index(4)}')


if __name__ == '__main__':
    main()
