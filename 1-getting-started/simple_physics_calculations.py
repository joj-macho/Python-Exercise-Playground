'''
Exercise: Simple Physics Calculations

This script performs simple physics calculations such as force, work,
and energy.

Formulas:
    Force: F = m * a (where m is mass, a is acceleration)
    Work: W = F * d (where F is force, d is displacement)
    Kinetic Energy: KE = 0.5 * m * v^2 (where m is mass, v is velocity)

Usage:
    Call the function with input values.

Tags: arithmetic operations, physics, force, work, energy
'''


def main():
    '''Perform simple physics calculations.'''
    mass = float(input('Enter mass (kg): '))
    acceleration = float(input('Enter acceleration (m/s^2): '))
    distance = float(input('Enter distance (m): '))
    velocity = float(input('Enter velocity (m/s): '))

    force = calculate_force(mass, acceleration)
    work = calculate_work(force, distance)
    kinetic_energy = calculate_kinetic_energy(mass, velocity)

    print(f'Force: {force:.2f} N')
    print(f'Work: {work:.2f} J')
    print(f'Kinetic Energy: {kinetic_energy:.2f} J')


def calculate_force(mass, acceleration):
    '''
    Calculates force using F = m * a.

    Parameters:
        mass (int/float): The mass of the object.
        acceleration (int/float): The acceleration of the object.

    Returns:
        float: The force on the object.
    '''
    return mass * acceleration


def calculate_work(force, distance):
    '''
    Calculate work using W = F * d.

    Parameters:
        force (int/float): The force on the object.
        distance (int/float): The distance the force acts upon.

    Returns:
        int/float: Work done on the object.
    '''
    return force * distance


def calculate_kinetic_energy(mass, velocity):
    '''
    Calculate kinetic energy using KE = 0.5 * m * v^2.

    Parameters:
        mass (int/float): The mass of the object.
        velocity (int/float): The velocity of the object.

    Returns:
        float: The kinetic energy of the object.
    '''
    return 0.5 * mass * velocity ** 2


if __name__ == '__main__':
    main()
