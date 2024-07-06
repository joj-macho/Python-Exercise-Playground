'''
Exercise: Next Day

This script determines the next day given a date.

Usage:
    Call the function with year, month, and day.

Tags: datetime module
'''

import datetime


def main():
    '''Determine the next day.'''
    year, month, day = 2024, 12, 31
    print(f'The next day is {get_next_day(year, month, day)}')


def get_next_day(year, month, day):
    '''
    Determines the next day given a date.

    Parameters:
        year (int): Year.
        month (int): Month.
        day (int): Day.

    Returns:
        str: Next day in YYYY-MM-DD format.
    '''
    date = datetime.date(year, month, day)
    next_day = date + datetime.timedelta(days=1)
    return next_day.strftime('%Y-%m-%d')


if __name__ == '__main__':
    main()
