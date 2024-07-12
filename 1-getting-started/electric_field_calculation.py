'''
Exercise: Electric Field Calculation

This script calculates the electric field produced by a point charge.

The electric field produced by a point charge is a vector field that
represents the effect of the charge on other charges around it.

Formula:
    E = k * Q / r^2,
where:
    - E is the electric field strength
    - k is Coulomb's constant (approximately 8.99 x 10^9 N m^2 C^-2)
    - Q is the charge of the point charge
    - r is the distance from the point charge

Usage:
    Call the function with charge and distance.

Tags: physics, electric fields, electromagnetism
'''


def main():
    '''Demonstrates electric field calculation.'''
    charge = 1e-6  # coulombs
    distance = 0.1  # meters
    field = electric_field(charge, distance)
    print(f'Electric field: {field:.2e} N/C')


def electric_field(charge, distance):
    '''
    Calculates the electric field produced by a point charge.

    Parameters:
        charge (float): Charge in coulombs.
        distance (float): Distance from the charge in meters.

    Returns:
        float: Electric field in N/C.
    '''
    k = 8.9875517923e9  # Coulomb's constant in N m^2/C^2
    return k * charge / distance**2


if __name__ == '__main__':
    main()
