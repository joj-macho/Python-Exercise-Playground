'''
Exercise: Average of Numbers

This script calculates the average of a given list of numbers.

Usage:
    Call the function with the list of numbers.

Tags: list, for loop, arithmetic operations, average
'''


def main():
    '''Calculate the average of a given list of numbers.'''
    numbers = [1, 2, 3, 4, 5]
    print(f'Average: {calculate_average(numbers)}')


def calculate_average(numbers):
    '''
    Calculates the average of numbers in a list.

    Parameters:
        numbers (list): The list of numbers.

    Returns:
        float: The average of the numbers.
    '''
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


if __name__ == '__main__':
    main()
