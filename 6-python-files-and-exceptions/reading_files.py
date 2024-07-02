'''
Exercise: Reading from Files

This script demonstrates how to read data from files.

Usage:
    Call the main function to see various examples of reading from files.

Tags: files, reading, basics
'''


def main():
    '''Demonstrates reading from files.'''
    with open('example.txt', 'r') as file:
        content = file.read()
        print('File content:')
        print(content)


if __name__ == '__main__':
    main()
