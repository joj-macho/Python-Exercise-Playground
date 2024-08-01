'''
Exercise: Format Date and Time

This script demonstrates how to format the current date and time in
different ways using the strftime method from the datetime module.

Usage:
    Call the main function to print the formatted date and time.

Tags: datetime module, strftime, date formatting, time formatting
'''

import datetime


def main():
    '''Formats and prints the current date and time using strftime.'''
    now = datetime.datetime.now()  # Current date and time

    # Default format
    print('Formatted Date and Time (default):',
          now.strftime('%Y-%m-%d %H:%M:%S'))

    # Different formats for date
    print('Formatted Date (YYYY-MM-DD):', now.strftime('%Y-%m-%d'))
    print('Formatted Date (DD-MM-YYYY):', now.strftime('%d-%m-%Y'))
    print('Formatted Date (Month DD, YYYY):', now.strftime('%B %d, %Y'))
    print('Formatted Date (Short Month DD, YYYY):', now.strftime('%b %d, %Y'))

    # Different formats for time
    print('Formatted Time (24-hour):', now.strftime('%H:%M:%S'))
    print('Formatted Time (12-hour):', now.strftime('%I:%M:%S %p'))

    # Full weekday name
    print('Weekday (Full name):', now.strftime('%A'))

    # Short weekday name
    print('Weekday (Short name):', now.strftime('%a'))

    # Full month name
    print('Month (Full name):', now.strftime('%B'))

    # Short month name
    print('Month (Short name):', now.strftime('%b'))

    # Locale's appropriate date and time representation
    print('Locale date and time:', now.strftime('%c'))

    # Locale's appropriate date representation
    print('Locale date:', now.strftime('%x'))

    # Locale's appropriate time representation
    print('Locale time:', now.strftime('%X'))


if __name__ == '__main__':
    main()
