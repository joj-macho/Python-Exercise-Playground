'''
Exercise: Reduce Measures

This script expresses imperial volume using the largest units possible.

Conversion references:
- 1 pint = 16 fluid ounces
- 1 quart = 2 pints
- 1 gallon = 4 quarts

Usage:
    Call the function with the volume in fluid ounces.

Tags: imperial measurements, arithmetic operators
'''


def main():
    '''Main function to express imperial volume using the largest units
    possible.'''
    fluid_ounces = 130
    gallons, quarts, pints, cups, ounces = reduce_measures(fluid_ounces)
    print(
        f'{fluid_ounces} fluid ounces is equivalent to {gallons} gallons, '
        f'{quarts} quarts, {pints} pints, {cups} cups, {ounces} fluid ounces'
    )


def reduce_measures(fluid_ounces):
    '''
    Expresses imperial volume using the largest units possible.

    Parameters:
        fluid_ounces (int): Volume in fluid ounces.

    Returns:
        tuple: The volume in gallons, quarts, pints, cups, and fluid ounces.
    '''
    gallons = fluid_ounces // 128
    fluid_ounces %= 128
    quarts = fluid_ounces // 32
    fluid_ounces %= 32
    pints = fluid_ounces // 16
    fluid_ounces %= 16
    cups = fluid_ounces // 8
    fluid_ounces %= 8
    ounces = fluid_ounces
    return gallons, quarts, pints, cups, ounces


if __name__ == '__main__':
    main()
