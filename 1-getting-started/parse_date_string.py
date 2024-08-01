'''
Exercise: Parse Date String

This script demonstrates how to convert various date and time strings into
datetime objects using the strptime method from the datetime module.

Usage:
    Call the main function to parse and print dates and times from strings.

Tags: datetime module, strptime, parse date string, date conversion
'''

import datetime


def main():
    '''Parses various date and time strings and prints the datetime objects.'''

    # Parse date string
    date_string = '2020-01-01'
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    print('Parsed Date:', date_obj)

    # Parse datetime string
    datetime_str = '2020-01-01 17:42:42'
    parsed_datetime = datetime.datetime.strptime(
        datetime_str, '%Y-%m-%d %H:%M:%S')
    print('Parsed Datetime:', parsed_datetime)

    # Parse date with different format
    date_string_alt = '01/01/2020'
    date_obj_alt = datetime.datetime.strptime(date_string_alt, '%d/%m/%Y')
    print('Parsed Date (alternative format):', date_obj_alt)

    # Parse time string
    time_string = '17:42:42'
    time_obj = datetime.datetime.strptime(time_string, '%H:%M:%S').time()
    print('Parsed Time:', time_obj)

    # Parse date and time with full month name
    datetime_str_full = 'January 01, 2020 17:42:42'
    parsed_datetime_full = datetime.datetime.strptime(
        datetime_str_full, '%B %d, %Y %H:%M:%S')
    print('Parsed Datetime (full month name):', parsed_datetime_full)

    # Parse date and time with short month name
    datetime_str_short = 'Jan 01, 2020 17:42:42'
    parsed_datetime_short = datetime.datetime.strptime(
        datetime_str_short, '%b %d, %Y %H:%M:%S')
    print('Parsed Datetime (short month name):', parsed_datetime_short)

    # Parse date with weekday name
    datetime_str_weekday = 'Wednesday, January 01, 2020 17:42:42'
    parsed_datetime_weekday = datetime.datetime.strptime(
        datetime_str_weekday, '%A, %B %d, %Y %H:%M:%S')
    print('Parsed Datetime (with weekday):', parsed_datetime_weekday)

    # Parse date with short weekday name
    datetime_str_weekday_short = 'Wed, Jan 01, 2020 17:42:42'
    parsed_datetime_weekday_short = datetime.datetime.strptime(
        datetime_str_weekday_short, '%a, %b %d, %Y %H:%M:%S')
    print('Parsed Datetime (short weekday):', parsed_datetime_weekday_short)


if __name__ == '__main__':
    main()
