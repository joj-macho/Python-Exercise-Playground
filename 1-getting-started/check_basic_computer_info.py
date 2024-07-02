'''
Exercise: Check Basic Computer Information

This script demonstrates how to use the platform module to retrieve and
display basic computer information such as machine type, processor,
and operating system.

Usage:
    Call the main function to retrieve and print basic information about the
    computer using the platform module.

Tags: platform module, system information, hardware details
'''

import platform


def main():
    '''Prints basic computer information.'''
    print('Machine Type:', platform.machine())
    print('Processor:', platform.processor())
    print('Operating System:', platform.system(), platform.release())
    print('Platform:', platform.platform())


if __name__ == '__main__':
    main()
