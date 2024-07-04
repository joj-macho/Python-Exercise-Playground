'''
Exercise: Projectile Motion Calculations

This script calculates the range and maximum height of a projectile.

Formulas:
    Range: R = (v^2 * sin(2 * theta)) / g
    Maximum Height: H = (v^2 * sin^2(theta)) / (2 * g)
where:
    - v is the initial velocity
    - theta is the angle of projection
    - g is the acceleration due to gravity (9.81 m/s^2)

Usage:
    Call the main function and follow the prompts.

Tags: math module, arithmetic operations, physics, projectile motion
'''

import math


def main():
    '''Calculate range and maximum height of a projectile.'''
    velocity = float(input('Enter the initial velocity (m/s): '))
    angle = float(input('Enter the angle of projection (degrees): '))

    range_proj, max_height = calculate_projectile_motion(velocity, angle)
    print(f'Range: {range_proj:.2f} meters')
    print(f'Maximum Height: {max_height:.2f} meters')


def calculate_projectile_motion(velocity, angle):
    '''
    Calculate the range and maximum height of a projectile.

    Parameters:
        velocity (int/float): Initial velocity of a projectile.
        angle (int/float): The angle of prjection in degrees.

    Returns:
        tuple: Tuple of range and maximum height of a projectile.
    '''
    g = 9.81

    angle_rad = math.radians(angle)  # degrees to radians

    range_proj = (velocity ** 2 * math.sin(2 * angle_rad)) / g
    max_height = (velocity ** 2 * math.sin(angle_rad) ** 2) / (2 * g)

    return range_proj, max_height


if __name__ == '__main__':
    main()
