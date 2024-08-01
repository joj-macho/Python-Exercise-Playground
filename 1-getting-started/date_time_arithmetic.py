'''
Exercise: Date and Time Arithmetic Operations

This script demonstrates various arithmetic operations on date and time
objects using the datetime module.
These operations include determining the start and end of the week, month,
and year, calculating the difference between dates, and adding or subtracting
days.

Usage:
    Call the main function to perform and print results of date and time
    arithmetic operations.

Tags: datetime module, date arithmetic, time arithmetic, timedelta,
date calculations
'''


import datetime


def main():
    '''Performs various arithmetic operations on date and time.'''

    # Difference between two dates
    date1 = datetime.date(2020, 1, 1)
    date2 = datetime.date(2020, 1, 31)
    difference = date2 - date1
    print('Difference between dates:', difference.days, 'days')

    # Add and subtract days
    date = datetime.date(2020, 1, 31)
    days_to_add = 10
    days_to_subtract = 5
    new_date_add = date + datetime.timedelta(days=days_to_add)
    new_date_subtract = date - datetime.timedelta(days=days_to_subtract)
    print('Original Date:', date)
    print('Date after adding days:', new_date_add)
    print('Date after subtracting days:', new_date_subtract)

    # Get start and end of the week for a given date
    start_of_week = date - datetime.timedelta(days=date.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)
    print('Start of the Week:', start_of_week)
    print('End of the Week:', end_of_week)

    # Get start and end of the month for a given date
    start_of_month = date.replace(day=1)
    next_month = start_of_month.replace(
        month=start_of_month.month % 12 + 1, day=1)
    end_of_month = next_month - datetime.timedelta(days=1)
    print('Start of the Month:', start_of_month)
    print('End of the Month:', end_of_month)

    # Get start and end of the year for a given date
    start_of_year = date.replace(month=1, day=1)
    end_of_year = date.replace(month=12, day=31)
    print('Start of the Year:', start_of_year)
    print('End of the Year:', end_of_year)

    # Calculate days until a future date
    future_date = datetime.date(2020, 12, 25)
    days_until_future_date = future_date - date
    print('Days until future date (Dec 25, 2020):',
          days_until_future_date.days)

    # Calculate days since a past date
    past_date = datetime.date(2019, 1, 1)
    days_since_past_date = date - past_date
    print('Days since past date (Jan 1, 2019):', days_since_past_date.days)


if __name__ == '__main__':
    main()
