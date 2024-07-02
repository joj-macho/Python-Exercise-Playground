'''
Exercise: Dictionary Methods

This script demonstrates various methods available for dictionaries.

Usage:
    Call the main function to see various examples of dictionary methods.

Tags: dictionaries, methods, basics
'''


def main():
    '''Demonstrates various dictionary methods.'''
    my_dict = {'name': 'Alice', 'age': 20, 'pet': 'cat'}
    print(f'Dictionary: {my_dict}')

    keys = my_dict.keys()
    print(f'Keys: {keys}')

    values = my_dict.values()
    print(f'Values: {values}')

    items = my_dict.items()
    print(f'Items: {items}')

    my_dict.update({'pet_age': '2'})
    print(f'After update: {my_dict}')


if __name__ == '__main__':
    main()
