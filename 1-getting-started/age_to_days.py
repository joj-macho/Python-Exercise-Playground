'''
Exercise: Converting Age to Number of Days

This script converts age in years to number of days.

Usage:
    Call the main function to convert age to days.

Tags: age conversion, days
'''


def main():
    '''Convert age to number of days.'''
    age_years = int(input('Enter your age in years: '))
    days_in_year = 365
    age_days = age_years * days_in_year

    print(f'Your age in days: {age_days} days')


if __name__ == '__main__':
    main()
