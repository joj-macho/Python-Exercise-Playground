'''
Exercise: Magic Dates

This script determines whether or not a date is a magic date.

A magic date is defined as a date where:
- day * month = year (last two digits)

Usage:
    Call the function with the day, month, and year.

Tags: 
'''


def main():
    '''Main function to determine whether or not a date is a magic date.'''
    day, month, year = 6, 10, 1960
    print(f'Is the date {day}/{month}/{year} a magic date? '
          f'{is_magic_date(day, month, year)}')


def is_magic_date(day, month, year):
    '''
    Determines whether or not a date is a magic date.

    Parameters:
        day (int): The day.
        month (int): The month.
        year (int): The year.

    Returns:
        bool: True if the date is magic, False otherwise.
    '''
    return day * month == int(str(year)[-2:])


if __name__ == '__main__':
    main()
