'''
Exercise: What Day of the Week Is January 1?

This script determines the day of the week for January 1 of any given year.

Usage:
    Call the function with a year value.

Tags: datetime module, calendar
'''

import datetime


def main():
    '''Main function to determine the day of the week for January 1.'''
    year = 2024
    print(f'January 1, {year} is a {get_day_of_week(year)}')


def get_day_of_week(year):
    '''
    Determines the day of the week for January 1.

    Parameters:
        year (int): Year.

    Returns:
        str: Day of the week.
    '''
    date = datetime.date(year, 1, 1)
    return date.strftime('%A')


if __name__ == '__main__':
    main()
