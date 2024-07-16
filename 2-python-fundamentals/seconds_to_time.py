'''
Exercise: Get Hours, Minutes, and Seconds

This script converts a total number of seconds to a string representing days,
hours, minutes, and seconds.

Usage:
    Call the function with the total number of seconds.

Tags: while loop, arithmetic operations, time conversion
'''


def main():
    '''Demonstrates time conversion.'''
    total_seconds = (24 * 3600 * 7) + (3600 * 7) + (60 * 7) + 7
    print(f'{total_seconds} seconds --> '
          f'{get_days_hours_minutes_seconds(total_seconds)}')


def get_days_hours_minutes_seconds(total_seconds):
    '''
    Convert total seconds to a string representing days, hours, minutes, and
    seconds.

    Parameters:
        total_seconds (int): Total number of seconds to convert.

    Returns:
        str: Time formatted string.
    '''
    # Starting with 0 seconds
    if total_seconds == 0:
        return '0d: 0h: 0m: 0s'

    days = 0
    while total_seconds >= 86400:
        days += 1
        total_seconds -= 86400

    hours = 0
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600

    minutes = 0
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60

    seconds = total_seconds
    return f'{days}d: {hours}h: {minutes}m: {seconds}s'


if __name__ == '__main__':
    main()
