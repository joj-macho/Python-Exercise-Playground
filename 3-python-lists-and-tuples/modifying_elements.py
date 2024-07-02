'''
Exercise: Modifying Elements

This script demonstrates how to modify elements in lists.

Usage:
    Call the main function to see various examples of modifying elements.

Tags: lists, modification, data structures
'''


def main():
    '''Demonstrates modifying elements in lists.'''
    my_list = [1, 2, 3, 4, 5]
    print(f'Original list: {my_list}')

    my_list[0] = 10
    print(f'Modified list: {my_list}')

    my_list.append(6)
    print(f'List after appending: {my_list}')

    my_list.remove(4)
    print(f'List after removing: {my_list}')


if __name__ == '__main__':
    main()
