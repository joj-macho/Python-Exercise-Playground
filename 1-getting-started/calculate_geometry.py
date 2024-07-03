'''
Exercise: Calculating Area, Perimeter, Volume, and Surface Area

This script demonstrates how to calculate the area and perimeter for a
rectangle and the volume and surface area for a rectangular prism (cuboid)
based on the length, width, and height of a shape.

Usage:
    Call the main function to see various calculations.

Tags: arithmetic operations, area, perimeter, volume, surface area
'''


def main():
    '''Demonstrates the calculation of area, perimeter, volume, and
    surface area.'''
    length = 5
    width = 3
    height = 4

    print(f'Area of rectangle: {calculate_area(length, width)}')
    print(f'Perimeter of rectangle: {calculate_perimeter(length, width)}')
    print(f'Volume of rectangular prism: '
          f'{calculate_volume(length, width, height)}')
    print(f'Surface area of rectangular prism: '
          f'{calculate_surface_area(length, width, height)}')


def calculate_area(length, width):
    '''
    Calculates the area of a rectangle.

    Parameters:
        length (int/float): The length of the shape.
        width (int/float): The width of the shape.

    Returns:
        int/float: The area of the shape.
    '''
    return length * width


def calculate_perimeter(length, width):
    '''
    Calculates the perimeter of a rectangle.

    Parameters:
        length (int/float): The length of the shape.
        width (int/float): The width of the shape.

    Returns:
        int/float: The perimeter of the shape.
    '''
    return 2 * (length + width)


def calculate_volume(length, width, height):
    '''
    Calculates the volume of a rectangular prism.

    Parameters:
        length (int/float): The length of the shape.
        width (int/float): The width of the shape.
        height (int/float): The height of the shape.

    Returns:
        int/float: The volume of the shape.
    '''
    return length * width * height


def calculate_surface_area(length, width, height):
    '''
    Calculates the surface area of a rectangular prism.

    Parameters:
        length (int/float): The length of the shape.
        width (int/float): The width of the shape.
        height (int/float): The height of the shape.

    Returns:
        int/float: The surface area of the shape.
    '''
    return 2 * (length * width + width * height + height * length)


if __name__ == '__main__':
    main()
