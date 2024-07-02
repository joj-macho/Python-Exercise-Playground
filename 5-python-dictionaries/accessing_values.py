'''
Exercise: Accessing Values

This script demonstrates how to access values in dictionaries.

Usage:
    Call the main function to see various examples of accessing values in
    dictionaries.

Tags: dictionaries, accessing values, basics
'''


def main():
    '''Demonstrates accessing values in dictionaries.'''
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print(f"Name: {my_dict['name']}")
    print(f"Age: {my_dict['age']}")
    print(f"City: {my_dict['city']}")

    print(f"Get method (name): {my_dict.get('name')}")
    print(f"Get method (country): {my_dict.get('country', 'Unknown')}")


if __name__ == '__main__':
    main()
