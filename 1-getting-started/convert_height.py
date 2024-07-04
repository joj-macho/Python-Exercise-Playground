'''
Exercise: Height Units Conversion

This script converts height units between feet and meters.

Conversion formulas:
- Feet to Meters: meters = feet * 0.3048
- Meters to Feet: feet = meters / 0.3048

Usage:
    Call the functions with the height value.

Tags: arithmetic operations, height conversion
'''


def main():
    '''Main function to convert height units.'''
    feet = 5.9
    print(f'{feet} feet is {feet_to_meters(feet):.3f} meters')
    meters = 1.8
    print(f'{meters} meters is {meters_to_feet(meters):.3f} feet')


def feet_to_meters(feet):
    '''
    Converts feet to meters.

    Parameters:
        feet (float): Height in feet.

    Returns:
        float: Height in meters.
    '''
    return feet * 0.3048


def meters_to_feet(meters):
    '''
    Converts meters to feet.

    Parameters:
        meters (float): Height in meters.

    Returns:
        float: Height in feet.
    '''
    return meters / 0.3048


if __name__ == '__main__':
    main()
