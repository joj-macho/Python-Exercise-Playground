'''
Exercise: Formatting Strings

This script demonstrates how to format strings in Python.

Usage:
    Call the main function to see various examples of formatting strings.

Tags: strings, formatting, basics
'''


def main():
    '''Demonstrates formatting strings.'''
    name = 'Alice'
    age = 20

    formatted_string = f'My name is {name} and I am {age} years old.'
    print(f'Formatted string: {formatted_string}')

    template = 'My name is {} and I am {} years old.'
    old_style_formatted_string = template.format(name, age)
    print(f'Old style formatted string: {old_style_formatted_string}')


if __name__ == '__main__':
    main()
