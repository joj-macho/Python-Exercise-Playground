'''
Exercise: Area of a circle

This script calculates the area and circumference of a circle.

Formulae:
    Area = π * r^2
    Circumference = 2 * π * r
where:
    - r is the radius of the circle.
    - π (pi) is a constant approximately equal to 3.14159.

Usage:
    Call the function with the radius value.

Tags: math module, arithmetic operations, area, circumference, circle
'''

import math


def main():
    '''Perform basic math calculations.'''
    radius = 5
    area = area_of_circle(radius)
    circumference = 2 * math.pi * radius

    print(f'Area of circle: {area:.2f}')
    print(f'Circumference of circle: {circumference:.2f}')


def area_of_circle(radius):
    '''
    Calculates the area of a circle.

    Parameters:
        radius (int/float): The radius of a circle.

    Returns:
        float: The area of a circle.
    '''
    return math.pi * radius ** 2


if __name__ == '__main__':
    main()
