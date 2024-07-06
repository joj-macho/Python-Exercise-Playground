'''
Exercise: Triangle Type

This script classifies a triangle as equilateral, isosceles, or scalene based
on the lengths of its sides.

Usage:
    Call the function with length values.

Tags: if-elif-else, triangle, classification
'''


def main():
    '''Classify the triangle based on its sides.'''
    a = float(input('Enter the length of side a: '))
    b = float(input('Enter the length of side b: '))
    c = float(input('Enter the length of side c: '))

    print(f'The triangle of sides {a}, {b}, and {c} is classified as: '
          f'{classify_triangle(a, b, c)}')


def classify_triangle(a, b, c):
    '''
    Classify a triangle based on its side lengths.

    Parameters:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        str: The type of triangle.
    '''
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isosceles'
    else:
        return 'Scalene'


if __name__ == '__main__':
    main()
