'''
Exercise: Adding and Removing Key-Value Pairs

This script demonstrates how to add and remove key-value pairs in dictionaries.

Usage:
    Call the main function to see various examples of adding and removing
    key-value pairs.

Tags: dictionaries, key-value pairs, basics
'''


def main():
    '''Demonstrates adding and removing key-value pairs in dictionaries.'''
    my_dict = {'name': 'Alice', 'age': 20}
    print(f'Original dictionary: {my_dict}')

    my_dict['pet'] = 'cat'
    print(f'After adding city: {my_dict}')

    del my_dict['age']
    print(f'After deleting age: {my_dict}')


if __name__ == '__main__':
    main()
