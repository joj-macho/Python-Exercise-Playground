'''
Exercise: Converting between Celsius and Fahrenheit

This script provides functions to convert temperatures between Celsius
and Fahrenheit.

Usage:
    Call the functions with the temperature value to convert.

Tags: arithmetic operations, temperature conversion, print()
'''


def main():
    '''Main function to demonstrate temperature conversion.'''
    celsius = 100
    fahrenheit = 32

    print(f'{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit.')
    print(f'{fahrenheit} Fahrenheit = '
          f'{fahrenheit_to_celsius(fahrenheit)} Celsius.')


def celsius_to_fahrenheit(celsius):
    '''
    Converts Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    '''
    # Formula: (Celsius * 9/5) + 32
    return (celsius * (9 / 5)) + 32


def fahrenheit_to_celsius(fahrenheit):
    '''
    Converts Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    '''
    # Formula: (Fahrenheit - 32) * 5/9
    return (fahrenheit - 32) * (5 / 9)


if __name__ == '__main__':
    main()
