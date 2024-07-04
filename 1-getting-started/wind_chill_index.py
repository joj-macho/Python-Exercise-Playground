'''
Exercise: Wind Chill Index

This script calculates the wind chill index given the air temperature
and wind speed using the formula:
Wind Chill Index (WCI): WCI = 13.12 + 0.6215 * T - 11.37 * V^0.16 + 0.3965
* T * V^0.16
where T is the air temperature in Celsius and V is the wind speed in km/h.

Calculation formula:
- WCI = 13.12 + 0.6215 * T - 11.37 * V^0.16 + 0.3965 * T * V^0.16

Usage:
    Call the function with the air temperature and wind speed.

Tags: arithmetic operations, wind chill, round()
'''


def main():
    '''Main function to calculate wind chill index.'''
    temperature, wind_speed = -5, 30
    wci = wind_chill(temperature, wind_speed)
    print(f'The wind chill index is {wci}')


def wind_chill(temperature, wind_speed):
    '''
    Calculates the wind chill index.

    Parameters:
        temperature (float): Air temperature in Celsius.
        wind_speed (float): Wind speed in kilometers per hour.

    Returns:
        int: Wind chill index rounded to the closest integer.
    '''
    wind_chill_index = (13.12 + 0.6215 * temperature -
                        11.37 * wind_speed ** 0.16 +
                        0.3965 * temperature * wind_speed ** 0.16)
    return round(wind_chill_index)


if __name__ == '__main__':
    main()
