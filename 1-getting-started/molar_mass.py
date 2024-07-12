'''
Exercise: Molar Mass Calculation

This script calculates the molar mass of a compound based on its molecular
formula.

The molar mass of a compound is the mass of one mole of the compound.

Formula:
    Molar Mass (M) = ∑ (Atomic Mass of Element x Number of Atoms of Element)

Usage:
    Call the function with a list of elements and their counts.

Tags: arithmetic operations, comprehension, chemistry, molecular formulas
'''


def main():
    '''Demonstrates molar mass calculation.'''
    elements_counts = {'H': 2, 'O': 1}  # Water (H2O)
    molar_mass = calculate_molar_mass(elements_counts)
    print(f'Molar mass: {molar_mass:.2f} g/mol')


def calculate_molar_mass(elements_counts):
    '''
    Calculates the molar mass of a compound.

    Parameters:
        elements_counts (dict): A dictionary where keys are element symbols
        and values are their counts.

    Returns:
        float: Molar mass of the compound.
    '''
    atomic_masses = {
        'H': 1.008, 'He': 4.0026, 'C': 12.011, 'O': 15.999, 'N': 14.007,
        'Na': 22.990, 'Cl': 35.45, 'S': 32.07, 'K': 39.098, 'Mg': 24.305
    }
    molar_mass = sum(atomic_masses[element] * count for element, count in
                     elements_counts.items())
    return molar_mass


if __name__ == '__main__':
    main()
