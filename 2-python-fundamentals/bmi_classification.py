'''
Exercise: BMI Classification

This script classifies a person's body mass index (BMI) as underweight,
normal weight, overweight, or obese.

Usage:
    Call the function with bmi value.

Tags: if-elif-else, BMI classification,
'''


def main():
    '''Calculate and classify BMI.'''
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    bmi = weight / (height ** 2)
    classification = classify_bmi(bmi)
    print(f'Your BMI is {bmi:.2f}, classified as: {classification}')


def classify_bmi(bmi):
    '''
    Classify BMI value.

    Parameters:
        bmi (float): The BMI value.

    Returns:
        str: The BMI classification.
    '''
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


if __name__ == '__main__':
    main()
