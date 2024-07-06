'''
Exercise: Roots of Quadratic Function

This script solves a quadratic equation and categorizes the roots based
on the discriminant.

Root classification based on the discriminant:
    - D > 0: Two distinct real roots.
    - D = 0: One real root (repeated).
    - D < 0: Two complex roots.

Usage:
    Call the function with coefficients a, b, and c.

Tags: if-elif-else, math module, mathematics, quadratic equation
'''

import math


def main():
    '''Solve a quadratic equation.'''
    a = 5
    b = -1
    c = 2

    roots, root_types = solve_quadratic_equation(a, b, c)
    print(f'Roots: {", ".join(map(str, roots))} ({root_types})')


def solve_quadratic_equation(a, b, c):
    '''
    Solves a quadratic equation and categorizes the roots based on the
    discriminant.

    Parameters:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple: Roots of the quadratic equation and their types.
    '''
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2), 'Real and distinct roots'
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,), 'Real and equal roots'
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return (f'{real_part} + {imaginary_part}i',
                f'{real_part} - {imaginary_part}i'), 'Complex roots'


if __name__ == '__main__':
    main()
