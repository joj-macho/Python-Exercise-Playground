'''
Exercise: Reverse String

This script provides a function to return the characters of a string
in reverse order.

Usage:
    Call the function with a string.

Tags: string
'''


def main():
    '''Main function to demonstrate string reversal.'''
    text = 'hello'
    print(f'Reversed string: {reverse_string(text)}')


def reverse_string(text):
    '''
    Reverses the characters in a string.

    Parameters:
        text (str): The input string.

    Returns:
        str: The reversed string.
    '''
    result = ''
    for char in text:
        result = char + result
    return result


if __name__ == '__main__':
    main()
