'''
Exercise: pH Calculation

This script calculates the pH of a solution based on its hydrogen ion
concentration.

The pH of a solution is a measure of its acidity or basicity.

Formula:
    pH = -log10[H+].
where
    [H+] is the concentration of hydrogen ions in moles per litre.

Usage:
    Call the function with the hydrogen ion concentration.

Tags: math(), chemistry, pH calculation, acidity
'''

import math


def main():
    '''Demonstrates pH calculation.'''
    h_concentration = 0.0001  # Example concentration (0.0001 M)
    ph = calculate_ph(h_concentration)
    print(f'pH of the solution: {ph:.2f}')


def calculate_ph(h_concentration):
    '''
    Calculates the pH of a solution.

    Parameters:
        h_concentration (float): Hydrogen ion concentration in mol/L.

    Returns:
        float: pH of the solution.
    '''
    return -math.log10(h_concentration)


if __name__ == '__main__':
    main()
