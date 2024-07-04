'''
Exercise: Calculating Area, Perimeter, Volume, and Surface Area

This script calculates the area, perimeter, volume, and surface area of
a cuboid given its length, width, and height.

Formulae:
    Area of a face: A = l * w
    Perimeter of a face: P = 2 * (l + w)
    Volume: V = l * w * h
    Surface Area: SA = 2 * (lw + lh + wh)
where:
    - l is the length of the cuboid.
    - w is the width of the cuboid.
    - h is the height of the cuboid.

Usage:
    Call the function with the length, width, and height values.

Tags: arithmetic operations, geometry, cuboid, area, perimeter, volume,
surface area
'''


def main():
    '''Demonstrates the calculation of area, perimeter, volume, and
    surface area.'''
    length = 5
    width = 3
    height = 4

    print(f'Area of a face: {calculate_area(length, width)}')
    print(f'Perimeter of a face: {calculate_perimeter(length, width)}')
    print(f'Volume of rectangular prism: '
          f'{calculate_volume(length, width, height)}')
    print(f'Surface area of rectangular prism: '
          f'{calculate_surface_area(length, width, height)}')


def calculate_area(length, width):
    '''
    Calculates the area of a face.

    Parameters:
        length (int/float): The length of the cuboid.
        width (int/float): The width of the cuboid.

    Returns:
        int/float: The area of the face.
    '''
    return length * width


def calculate_perimeter(length, width):
    '''
    Calculates the perimeter of a face.

    Parameters:
        length (int/float): The length of the cuboid.
        width (int/float): The width of the cuboid.

    Returns:
        int/float: The perimeter of the face.
    '''
    return 2 * (length + width)


def calculate_volume(length, width, height):
    '''
    Calculates the volume of a cuboid.

    Parameters:
        length (int/float): The length of the cuboid.
        width (int/float): The width of the cuboid.
        height (int/float): The height of the cuboid.

    Returns:
        int/float: The volume of the cuboid.
    '''
    return length * width * height


def calculate_surface_area(length, width, height):
    '''
    Calculates the surface area of a cuboid.

    Parameters:
        length (int/float): The length of the cuboid.
        width (int/float): The width of the cuboid.
        height (int/float): The height of the cuboid.

    Returns:
        int/float: The surface area of the cuboid.
    '''
    return 2 * (length * width + width * height + height * length)


if __name__ == '__main__':
    main()
