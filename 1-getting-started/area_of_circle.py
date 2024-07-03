'''
Exercise: Area of a circle

This script calculates the area and circumference of a circle.

Usage:
    Call the function with the radius parameter to get the area.

Tags: math module, area of circle, circumference, radius
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
