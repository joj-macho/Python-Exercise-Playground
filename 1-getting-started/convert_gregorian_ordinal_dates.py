'''
Exercise: Convert Gregorian Date and Ordinal Dates

This script converts between Gregorian date and ordinal date.

Gregorian Date: A calendar date in the format (YYYY-MM-DD).
Ordinal Date: A date represented by the number of days from January 1st of the same year.

Usage:
    Call the functions with the date values.

Tags: datetime module, gregorian date, ordinal date
'''

import datetime


def main():
    '''Main function to convert between Gregorian date and ordinal date.'''
    year, month, day = 2024, 6, 18
    ordinal_date = gregorian_to_ordinal(year, month, day)
    print(f'The ordinal date for {year}-{month}-{day} is {ordinal_date}')

    ordinal_year, ordinal_day = 2024, 170
    gregorian_date = ordinal_to_gregorian(ordinal_year, ordinal_day)
    print(f'The Gregorian date for {ordinal_year} day {ordinal_day} is '
          f'{gregorian_date}')


def gregorian_to_ordinal(year, month, day):
    '''
    Converts Gregorian date to ordinal date.

    Parameters:
        year (int): The year.
        month (int): The month.
        day (int): The day.

    Returns:
        int: The ordinal date.
    '''
    date = datetime.date(year, month, day)
    return date.timetuple().tm_yday


def ordinal_to_gregorian(year, ordinal_day):
    '''
    Converts ordinal date to Gregorian date.

    Parameters:
        year (int): The year.
        ordinal_day (int): The ordinal day.

    Returns:
        str: The Gregorian date in 'Month Day' format.
    '''
    date = datetime.date(year, 1, 1) + datetime.timedelta(days=ordinal_day - 1)
    return date.strftime('%B %d')


if __name__ == '__main__':
    main()
