'''
Exercise: Free Fall Velocity

This script determines how quickly an object is travelling when it hits
the ground after falling from a given height using the formula:

Formula:
    v = sqrt(2 * g * h)
where:
    - v is the final velocity.
    - g is the acceleration due to gravity (9.81 m/s^2 on Earth).
    - h is the height in meters

Usage:
    Call the function with the height value.

Tags: math module, arithmetic operations, free fall, velocity
'''

import math


def main():
    '''Main function to calculate the velocity of an object in free fall.'''
    height = 20
    velocity = free_fall_velocity(height)
    print(f'Final velocity of a free falling object = {velocity:.3f} m/s')


def free_fall_velocity(height):
    '''
    Calculates the final velocity of an object in free fall.

    Parameters:
        height (float): Height from which the object falls in meters.

    Returns:
        float: Final velocity of the object in meters per second.
    '''
    g = 9.81  # Acceleration due to gravity in m/s²
    velocity = math.sqrt(2 * g * height)
    return velocity


if __name__ == '__main__':
    main()
