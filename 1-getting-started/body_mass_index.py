'''
Exercise: Body Mass Index

This script calculates the Body Mass Index (BMI) given the weight and height
of a person.
BMI = weight in kg / (height in m)^2

Usage:
    Call the function with the weight and height.

Tags: arithmetic operations, bmi
'''


def main():
    '''Main function to calculate BMI.'''
    weight, height = 70, 1.75
    print(f'The BMI is {calculate_bmi(weight, height):.2f}')


def calculate_bmi(weight, height):
    '''
    Calculates the Body Mass Index (BMI).

    Parameters:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: The body mass index of a person.
    '''
    return weight / (height ** 2)


if __name__ == '__main__':
    main()
