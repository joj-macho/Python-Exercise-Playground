'''
Exercise: Check Current Date and Time

This script demonstrates how to check the current date and time using the
datetime module.
This is useful for time-stamping outputs and logging events in your scripts.

Usage:
    Call the main function to print the current date and time.

Tags: datetime module, current date and time, time-stamping, logging events
'''

import datetime


def main():
    '''Prints the current date and time using datetime module.'''
    now = datetime.datetime.now()  # Current date and time
    today = datetime.date.today()  # Today's date

    print('Today\'s Date:', today)
    print('Current Date and Time:', now)
    print('Current Date:', now.date())
    print('Current Time:', now.time())


if __name__ == '__main__':
    main()
