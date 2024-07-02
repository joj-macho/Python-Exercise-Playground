'''
Exercise: Iterating Through Dictionaries

This script demonstrates how to iterate through dictionaries.

Usage:
    Call the main function to see various examples of iterating through
    dictionaries.

Tags: dictionaries, iteration, basics
'''


def main():
    '''Demonstrates iterating through dictionaries.'''
    my_dict = {'name': 'Alice', 'age': 20, 'pet': 'cat'}

    print('Iterating through keys:')
    for key in my_dict:
        print(f'Key: {key}')

    print('Iterating through values:')
    for value in my_dict.values():
        print(f'Value: {value}')

    print('Iterating through items:')
    for key, value in my_dict.items():
        print(f'Key: {key}, Value: {value}')


if __name__ == '__main__':
    main()
