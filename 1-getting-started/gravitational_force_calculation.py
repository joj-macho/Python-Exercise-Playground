'''
Exercise: Gravitational Force Calculation

This script calculates the gravitational force between two masses.

The gravitational force between two masses is a fundamental concept in
physics that describes the attractive force between two objects with mass.

Formula:
    F = G * m1 * m2 / r^2
where:
    - F is the gravitational force between the two masses
    - G is the universal gravitational constant
    - m1 and m2 are the masses of the two objects
    - r is the distance between the centers of the two objects

Usage:
    Call the function with masses and distance.

Tags: physics, gravitation, force calculations
'''


def main():
    '''Demonstrates gravitational force calculation.'''
    m1 = 5.972e24  # mass of Earth in kilograms
    m2 = 7.348e22  # mass of Moon in kilograms
    distance = 3.844e8  # distance between Earth and Moon in meters
    force = gravitational_force(m1, m2, distance)
    print(f'Gravitational force: {force:.2e} N')


def gravitational_force(m1, m2, distance):
    '''
    Calculates the gravitational force between two masses.

    Parameters:
        m1 (float): Mass of the first object in kilograms.
        m2 (float): Mass of the second object in kilograms.
        distance (float): Distance between the objects in meters.

    Returns:
        float: Gravitational force in newtons.
    '''
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    return G * m1 * m2 / distance**2


if __name__ == '__main__':
    main()
