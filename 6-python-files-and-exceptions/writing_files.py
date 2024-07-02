'''
Exercise: Writing to Files

This script demonstrates how to write data to files.

Usage:
    Call the main function to see various examples of writing to files.

Tags: files, writing, basics
'''


def main():
    '''Demonstrates writing to files.'''
    with open('output.txt', 'w') as file:
        file.write('Hello, World!\n')
        file.write('This is a test file.')

    print('Data written to output.txt')


if __name__ == '__main__':
    main()
