'''
Exercise: Concentration Calculation

This script calculates the concentration of a solution.

Formula:
    C = m/V
where:
    - C is the concentration,
    - m is the mass of the solute dissolved,
    - and V is the total volume of the solution.

Usage:
    Call the function with amount of solute and volume of solution.

Tags: chemistry, concentration, solutions
'''


def main():
    '''Demonstrates concentration calculation.'''
    amount_of_solute = 5.0  # grams
    volume_of_solution = 2.0  # liters
    concentration_value = concentration(amount_of_solute, volume_of_solution)
    print(f'Concentration: {concentration_value:.2f} g/L')


def concentration(amount_of_solute, volume_of_solution):
    '''
    Calculates the concentration of a solution.

    Parameters:
        amount_of_solute (float): Amount/mass of solute in grams.
        volume_of_solution (float): Volume of solution in liters.

    Returns:
        float: Concentration in g/L.
    '''
    return amount_of_solute / volume_of_solution


if __name__ == '__main__':
    main()
