'''
Exercise: Convert Pressure Units

This script demonstrates how to convert pressure from Pascals to other units
of pressure such as bar, atm, torr, and psi.

Conversions:
- 1 Pascal (Pa) = 0.00001 bar
- 1 Pascal (Pa) = 9.86923e-6 atm
- 1 Pascal (Pa) = 0.00750062 torr
- 1 Pascal (Pa) = 0.000145038 psi

Usage:
    Call the main function and pass the pressure in Pascals.

Tags: arithmetic operations, pressure conversion, units
'''


def main():
    '''Main function to convert pressure units.'''
    pascals = 101325
    print(f"{pascals:,} Pa {'=':>3} {pascals_to_bar(pascals):.5f} bar")
    print(f"{'=':>14} {pascals_to_atm(pascals):.5f} atm")
    print(f"{'=':>14} {pascals_to_torr(pascals):.5f} torr")
    print(f"{'=':>14} {pascals_to_psi(pascals):.5f} psi")


def pascals_to_bar(pascals):
    '''
    Converts pressure from Pascals to Bar.

    Parameters:
        pascals (float): Pressure in Pascals.

    Returns:
        float: Pressure in Bar.
    '''
    return pascals / 100000


def pascals_to_atm(pascals):
    '''
    Converts pressure from Pascals to Atmospheres.

    Parameters:
        pascals (float): Pressure in Pascals.

    Returns:
        float: Pressure in Atmospheres.
    '''
    return pascals / 101325


def pascals_to_torr(pascals):
    '''
    Converts pressure from Pascals to Torr.

    Parameters:
        pascals (float): Pressure in Pascals.

    Returns:
        float: Pressure in torr.
    '''
    return pascals / 133.322312022


def pascals_to_psi(pascals):
    '''
    Converts pressure from Pascals to Pounds per Square Inch.

    Parameters:
        atmospheres (float): Pressure in atmospheres.

    Returns:
        float: Pressure in Pounds per Square Inch.
    '''
    return pascals / 6894.744825494


if __name__ == '__main__':
    main()
