'''
Exercise: Check Environment Variables

This script demonstrates how to access and print environment variables using
the os module.
Environment variables are key-value pairs used to configure the operating
system and applications.

Usage:
    Call the main function to print all environment variables accessible
    to the current process.

Tags: environment variables, os module, system information
'''

import os  # To interact with the operating system


def main():
    '''Prints all environment variables.'''
    for key, value in os.environ.items():
        print(f'{key}: {value}')

    # Print a specific environment variable
    print('\nPATH Environment Variable:', os.getenv('PATH'))


if __name__ == '__main__':
    main()
