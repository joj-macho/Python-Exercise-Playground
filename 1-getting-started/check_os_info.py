'''
Exercise: Check Operating System Details

This script demonstrates how to check detailed operating system information
using the os module.
It includes details like the OS name, user name, and current working directory.

Usage:
    Call the main function to print detailed information about the
    operating system.

Tags: operating system details, os module, system information
'''

import os


def main():
    '''Retrieves and prints detailed operating system information.'''
    print('OS Name:', os.name)
    print('User Name:', os.getlogin())
    print('Current Working Directory:', os.getcwd())
    print('Files in Current Directory:', os.listdir('.'))


if __name__ == '__main__':
    main()
