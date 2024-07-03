'''
Exercise: Number Formatting and Alignment

This script demonstrates number formatting and alignment with f-strings
and format().

Usage:
    Call the main function.

Tags: number formatting, f-strings, format(), alignment
'''


def main():
    '''Format and align numbers.'''
    number = 1234.56789
    print(f'Number formatted with f-string: {number:.2f}')
    print('Number formatted with format(): {:.2f}'.format(number))

    print(f'Aligned to right: {number:>21.2f}')
    print(f'Aligned to left: {number:<10.2f}')


if __name__ == '__main__':
    main()
