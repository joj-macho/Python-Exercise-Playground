'''
Exercise: State of Water

This script determines the state of water (solid, liquid, gas) based on
temperature and pressure.

Water state classification:
    - Solid: Temperature <= 0°C and Pressure = 1 atm
    - Liquid: 0°C < Temperature < 100°C and Pressure = 1 atm
    - Gas: Temperature >= 100°C and Pressure = 1 atm

Usage:
    Call the function with temperature (in Celsius) and pressure (in atm).

Tags: if-elif-else, physics, chemistry, water state
'''


def main():
    '''Determine the state of water.'''
    temperature = 25
    pressure = 1
    print(f'The state of water at {temperature}°C and {pressure} atm is '
          f'{get_water_state(temperature, pressure)}')


def get_water_state(temperature, pressure):
    '''
    Determines the state of water based on temperature and pressure.

    Parameters:
        temperature (float): Temperature in Celsius.
        pressure (float): Pressure in atm.

    Returns:
        str: State of water.
    '''
    if temperature <= 0 and pressure == 1:
        return 'Solid'
    elif 0 < temperature < 100 and pressure == 1:
        return 'Liquid'
    elif temperature >= 100 and pressure == 1:
        return 'Gas'
    else:
        return 'Unknown'


if __name__ == '__main__':
    main()
