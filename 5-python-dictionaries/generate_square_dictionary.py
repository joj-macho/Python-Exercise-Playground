'''
Exercise: Generate Dictionary of (i, i*i) for Numbers from 1 to n

This script generates a dictionary that contains (i, i*i) such that i is an
integral number between 1 and n (both included).

Usage:
    Run the script and enter a number n when prompted.

Tags: dictionary
'''


def main():
    '''
    Main function to execute the script.
    '''
    n = int(input('Enter an integer: '))
    result = generate_square_dict(n)
    print(result)


def generate_square_dict(n):
    '''
    Generates a dictionary with (i, i*i) for numbers from 1 to n.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    dict: Dictionary containing (i, i*i) pairs.
    '''
    return {i: i * i for i in range(1, n + 1)}


if __name__ == '__main__':
    main()
