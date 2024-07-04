'''
Exercise: Distance Between Two Points

This script calculates the distance between two points in a 2D space.

Distance Formula: 
- distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

Usage:
    Call the function with the point coordinates.

Tags: math module, distance, 2D space, coordinates
'''

import math


def main():
    '''Calculate distance between two points.'''
    x1, y1, x2, y2 = 4, 3, 5, 2

    distance = calculate_distance(x1, y1, x2, y2)
    print(f'The distance between the points is {distance:.2f}')


def calculate_distance(x1, y1, x2, y2):
    '''
    Calculate distance between two points (x1, y1) and (x2, y2).

    Parameters:
        x1 (int/float): The x-coordinate of the first point.
        y1 (int/float): The y-coordinate of the first point.
        x2 (int/float): The x-coordinate of the second point.
        y2 (int/float): The y-coordinate of the second point.

    Returns:
        float: The distance between the two points.
    '''
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    main()
