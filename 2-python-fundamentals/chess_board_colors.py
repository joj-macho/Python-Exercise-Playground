'''
Exercise: Chess Board Colors

This script determines the color of a square on a chess board given its
column and row.

Chess board colors:
    - The squares on a chess board alternate between black and white.
    - The bottom-left square (a1) is always black.

Usage:
    Call the function with column and row numbers to get the color.

Tags: if-else, for loop, arithmetic operations, game, chess
'''


def main():
    '''Determine the color in chess board.'''
    for row in range(8):
        for column in range(8):
            color = get_square_color(column, row)
            print(f'Square ({column}, {row}) is {color}.')


def get_square_color(column, row):
    '''
    Determines the color of a square on a chess board.

    Parameters:
        column (int): The column of the square.
        row (int): The row of the square.

    Returns:
        str: The color of the square ('black' or 'white') or an
             empty string if out of bounds.
    '''
    if not (0 <= column <= 7) or not (0 <= row <= 7):
        return ''
    return 'white' if (column + row) % 2 == 0 else 'black'


if __name__ == '__main__':
    main()
