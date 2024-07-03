'''
Exercise: Converting Seconds to Days, Hours, Minutes, Seconds

This script converts seconds to days, hours, minutes, and seconds.

Usage:
    Call the function with the total seconds to convert.

Tags: time conversion, arithmetic operations
'''


def main():
    '''Demonstrates time conversion.'''
    total_seconds = (24 * 3600 * 7) + (3600 * 7) + (60 * 7) + 7
    print(f'{total_seconds:,} seconds --> '
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

    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f'{days}d: {hours}h: {minutes}m: {seconds}s'


if __name__ == '__main__':
    main()
