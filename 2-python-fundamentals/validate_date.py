'''
Exercise: Validate Date

This script provides a function to check if a date is valid.

A valid date must satisfy the following conditions:
    - The month must be between 1 and 12.
    - The day must be within the valid range for the given month.
    - For February, the day must be within the range considering leap years.

Usage:
    Call the function with the day, month, and year.

Tags: if-elif, date, validation, leap year
'''


def main():
    '''Demonstrate date validation.'''
    day, month, year = 31, 6, 2012
    print(f'Is {day}/{month}/{year} a valid date? '
          f'{is_valid_date(day, month, year)}')


def is_valid_date(day, month, year):
    '''
    Checks if a date is valid.

    Parameters:
        day (int): The day of the date.
        month (int): The month of the date.
        year (int): The year of the date.

    Returns:
        bool: True if date is valid, False otherwise.
    '''
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    # Check for valid leap year days
    if is_leap_year(year) and month == 2 and day == 29:
        return True

    # Check valid dates for 31 day months
    if month in (1, 3, 5, 7, 8, 10, 12) and (1 <= day <= 31):
        return True
    # Check valid dates for 30 day months
    elif month in (4, 6, 9, 11) and (1 <= day <= 30):
        return True
    # Check valid date for Feb
    elif month == 2 and (1 <= day <= 28):
        return True
    # All other dates should be invalid
    return False


def is_leap_year(year):
    '''
    Checks if a year is a leap year.

    Parameters:
        year (int): The year of the date to check.

    Returns:
        bool: True if year is a leap year, False otherwise.
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


if __name__ == '__main__':
    main()
