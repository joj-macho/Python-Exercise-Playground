'''
Exercise: Convert Pressure Units

This script converts pressure from Pascals (Pa) to other units of pressure:
bar, atm, torr, and psi.

Conversion Formulas:
    1 Pa = 1e-5 bar
    1 Pa = 9.86923e-6 atm
    1 Pa = 7.50062e-3 torr
    1 Pa = 1.45038e-4 psi

Usage:
    Call the function with the pressure value in Pascals.

Tags: arithmetic operations, pressure conversion
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
