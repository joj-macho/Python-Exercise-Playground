'''
Exercise: Boiling Point of Water

This script determines the boiling point of water at different altitudes.

The boiling point of water decreases with increasing altitude due to the
decrease in atmospheric pressure.

Using an approximation formula to determine the boiling point:
    BP = 100 - (altitude / 300)
where:
    - BP is the boiling point in degrees Celsius.
    - altitude is the altitude in meters.

Usage:
    Call the function with an altitude value.

Tags: if-else, physics, boiling point, altitude
'''


def main():
    '''Determine the boiling point of water at different altitudes.'''
    altitude = 1905
    print(f'The boiling point of water at {altitude} meters is '
          f'{get_boiling_point(altitude):.2f}°C')


def get_boiling_point(altitude):
    '''
    Determines the boiling point of water at different altitudes.

    Parameters:
        altitude (int): Altitude in meters.

    Returns:
        float: Boiling point in Celsius.
    '''
    if altitude <= 0:
        return 100
    else:
        return 100 - (altitude / 300)


if __name__ == '__main__':
    main()
