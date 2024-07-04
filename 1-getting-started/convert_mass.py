'''
Exercise: Mass Units Conversion

This script converts mass units between pounds and kilograms.

Conversion Formulas:
    Pounds to Kilograms: kg = lbs * 0.45359237
    Kilograms to Pounds: lbs = kg / 0.45359237

Usage:
    Call the functions with the mass value.

Tags: arithmetic operations, mass conversion
'''


def main():
    '''Main function to convert mass units.'''
    pounds = 150
    print(f'{pounds} pounds is {pounds_to_kilograms(pounds):.3f} kilograms.')
    kilograms = 68.04
    print(f'{kilograms} kilograms is {kilograms_to_pounds(kilograms):.3f} '
          'pounds.')


def pounds_to_kilograms(pounds):
    '''
    Converts pounds to kilograms.

    Parameters:
        pounds (float): Mass in pounds.

    Returns:
        float: Mass in kilograms.
    '''
    return pounds * 0.45359237


def kilograms_to_pounds(kilograms):
    '''
    Converts kilograms to pounds.

    Parameters:
        kilograms (float): Mass in kilograms.

    Returns:
        float: Mass in pounds.
    '''
    return kilograms / 0.45359237


if __name__ == '__main__':
    main()
