'''
Exercise: Check Leap Year

This script demonstrates how to determine if a given year is a leap year.

Usage:
    Call the main function to check and print if a year is a leap year.

Tags: datetime module, leap year, year check
'''


def main():
    '''Checks if a given year is a leap year and prints the result.'''
    year = 2024
    leap = is_leap_year(year)

    print(f'Is {year} a leap year?:', leap)


def is_leap_year(year):
    '''Returns True if the given year is a leap year, otherwise False.'''
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


if __name__ == '__main__':
    main()
