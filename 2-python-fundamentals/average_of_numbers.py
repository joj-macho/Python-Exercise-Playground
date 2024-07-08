'''
Exercise: Average of Numbers

This script calculates the average of a given list of numbers using a for
loop.

Usage:
    Call the function with the list of numbers.

Tags: for loop, arithmetic operations, average
'''


def main():
    '''Calculate the average of a given list of numbers.'''
    numbers = input('Enter a list of numbers separated by spaces: ').split()
    numbers = [int(num) for num in numbers]
    print(f'The average of the numbers in the list is '
          f'{calculate_average(numbers):.2f}')


def calculate_average(numbers):
    '''
    Calculates the average of a given list of numbers.

    Parameters:
        numbers (list): The list of numbers.

    Returns:
        float: The average of the numbers in the list.
    '''
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


if __name__ == '__main__':
    main()
