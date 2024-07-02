'''
Exercise: Python Operators

This script demonstrates various Python operators (arithmetic, comparison,
logical, and bitwise) and their usage.

Usage:
    Call the main function to see various operators and their usage.

Tags: operators, arithmetic operations, comparison, logical operations,
bitwise operations
'''


def main():
    '''Demonstrates various Python operators.'''
    a = 4
    b = 2

    # Arithmetic operators
    print(f'Sum: {a + b}')
    print(f'Difference: {a - b}')
    print(f'Product: {a * b}')
    print(f'Division: {a / b}')
    print(f'Floor Division: {a // b}')
    print(f'Modulus: {a % b}')
    print(f'Exponentiation: {a ** b}')

    # Comparison operators
    print(f'Is {a} greater than {b}? {a > b}')
    print(f'Is {a} less than or equal to {b}? {a <= b}')
    print(f'Is {a} equal to {b}? {a == b}')
    print(f'Is {a} not equal to {b}? {a != b}')

    # Logical operators
    x = True
    y = False
    print(f'Logical AND: {x and y}')
    print(f'Logical OR: {x or y}')
    print(f'Logical NOT: {not x}')

    # Bitwise operators (example)
    print(f'Bitwise AND: {a & b}')
    print(f'Bitwise OR: {a | b}')
    print(f'Bitwise XOR: {a ^ b}')
    print(f'Bitwise NOT: {~a}')
    print(f'Left Shift: {a << b}')
    print(f'Right Shift: {a >> b}')


if __name__ == '__main__':
    main()
