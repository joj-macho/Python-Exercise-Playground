'''
Exercise: Escaping Characters

This script demonstrates how to escape characters within strings.

Usage:
    Call the main function to see various examples of escaping characters.

Tags: strings, escaping, basics
'''


def main():
    '''Demonstrates escaping characters in strings.'''
    string_with_quotes = 'He said, "Hello, World!"'
    print(f'String with quotes: {string_with_quotes}')

    string_with_newline = 'Hello,\nWorld!'
    print(f'String with newline:\n{string_with_newline}')

    string_with_tab = 'Hello,\tWorld!'
    print(f'String with tab:\n{string_with_tab}')


if __name__ == '__main__':
    main()
