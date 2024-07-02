'''
Exercise: Python Keywords

This script prints a list of all Python keywords using the keyword module.

Usage:
    Call the main function to print a list of all Python keywords.

Tags: keyword module, keywords, basic Python, language fundamentals, print()
'''

import keyword


def main():
    '''Prints all Python keywords.'''
    # Get list of Python keywords
    keywords = keyword.kwlist
    print('All Python Keywords:', keywords)


if __name__ == '__main__':
    main()
