'''
Exercise: Temperature Conversion

This script converts temperature between Celsius, Fahrenheit, and Kelvin.

Conversion Formulas:
    - Celsius to Fahrenheit: F = C * 9/5 + 32
    - Fahrenheit to Celsius: C = (F - 32) * 5/9
    - Celsius to Kelvin: K = C + 273.15
    - Kelvin to Celsius: C = K - 273.15

Usage:
    Call the function with a temperature value and the current and target units

Tags: if-elif-else, arithmetic operations, temperature conversion
'''


def main():
    '''Convert temperature between units.'''
    temperature = 100
    from_unit = 'C'
    to_unit = 'F'
    print(f'The temperature in {to_unit} is '
          f'{convert_temperature(temperature, from_unit, to_unit)}')


def convert_temperature(temperature, from_unit, to_unit):
    '''
    Converts temperature between units.

    Parameters:
        temperature (float): Temperature value.
        from_unit (str): Current unit ('C', 'F', 'K').
        to_unit (str): Target unit ('C', 'F', 'K').

    Returns:
        float: Converted temperature.
    '''
    if from_unit == 'C':
        if to_unit == 'F':
            return temperature * 9 / 5 + 32
        elif to_unit == 'K':
            return temperature + 273.15
        else:
            return temperature
    elif from_unit == 'F':
        if to_unit == 'C':
            return (temperature - 32) * 5 / 9
        elif to_unit == 'K':
            return (temperature - 32) * 5 / 9 + 273.15
        else:
            return temperature
    elif from_unit == 'K':
        if to_unit == 'C':
            return temperature - 273.15
        elif to_unit == 'F':
            return (temperature - 273.15) * 9 / 5 + 32
        else:
            return temperature
    else:
        return 'Invalid units'


if __name__ == '__main__':
    main()
