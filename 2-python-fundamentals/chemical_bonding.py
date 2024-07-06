'''
Exercise: Chemical Bonding Type

This script determines the type of chemical bond based on electronegativity
difference.

Chemical bond classification:
    - Nonpolar Covalent: ΔEN < 0.5
    - Polar Covalent: 0.5 <= ΔEN < 1.7
    - Ionic: ΔEN >= 1.7

Usage:
    Call the function with electronegativity difference.

Tags: if-elif-else, chemistry, chemical bonding
'''


def main():
    '''Determine the type of chemical bond.'''
    difference = 1.1
    print(f'The type of chemical bond is {classify_bond_type(difference)}')


def classify_bond_type(difference):
    '''
    Determines the type of chemical bond based on electronegativity difference.

    Parameters:
        difference (float): Electronegativity difference.

    Returns:
        str: Bond type ('Ionic', 'Polar covalent', 'Nonpolar covalent').
    '''
    if difference >= 1.7:
        return 'Ionic'
    elif 0.5 <= difference < 1.7:
        return 'Polar covalent'
    else:
        return 'Nonpolar covalent'


if __name__ == '__main__':
    main()
