'''
Exercise: Head and Tail of a File

This script displays the first and last lines of a file.

Usage:
    Call the functions with the filename.

Tags: file
'''


def main():
    '''Display the first and last lines of a file.'''
    filename = 'example.txt'
    print(f'First line: {head(filename)}')
    print(f'Last line: {tail(filename)}')


def head(filename):
    '''
    Displays the first line of a file.

    Parameters:
        filename (str): The name of the file.

    Returns:
        str: The first line of the file.
    '''
    with open(filename, 'r') as file:
        return file.readline().strip()


def tail(filename):
    '''
    Displays the last line of a file.

    Parameters:
        filename (str): The name of the file.

    Returns:
        str: The last line of the file.
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines[-1].strip() if lines else ''


if __name__ == '__main__':
    main()
