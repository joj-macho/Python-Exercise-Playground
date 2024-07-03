'''
Exercise: Check Python Version

This script demonstrates how to check the version of Python that is currently
installed and being used to run your scripts.

Usage:
    Call the main function to get the version of Python currently installed.

Tags: Python version, sys module, basic script
'''

import sys


def main():
    '''Prints Python version information.'''
    print('Python Version:', sys.version)
    print('Python Version Info:', sys.version_info)


if __name__ == '__main__':
    main()
