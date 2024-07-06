'''
Exercise: Blood Pressure Classification

This script classifies blood pressure based on systolic and diastolic values.

Blood pressure classification:
    - Normal: Systolic < 120 and Diastolic < 80
    - Elevated: Systolic 120-129 and Diastolic < 80
    - Hypertension Stage 1: Systolic 130-139 or Diastolic 80-89
    - Hypertension Stage 2: Systolic >= 140 or Diastolic >= 90
    - Hypertensive Crisis: Systolic > 180 and/or Diastolic > 120

Usage:
    Call the function with systolic and diastolic values.

Tags: if-elif-else, health, blood pressure
'''


def main():
    '''Classify blood pressure.'''
    systolic = 180
    diastolic = 125
    print(f'The blood pressure {systolic}/{diastolic} mmHg is '
          f'{classify_blood_pressure(systolic, diastolic)}')


def classify_blood_pressure(systolic, diastolic):
    '''
    Classifies blood pressure based on systolic and diastolic values.

    Parameters:
        systolic (int): Systolic blood pressure in mmHg.
        diastolic (int): Diastolic blood pressure in mmHg.

    Returns:
        str: Blood pressure classification.
    '''
    if systolic < 90 or diastolic < 60:
        return 'Low'
    elif 90 <= systolic < 120 and 60 <= diastolic < 80:
        return 'Normal'
    elif 120 <= systolic < 130 and 60 <= diastolic < 80:
        return 'Elevated'
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return 'Hypertension Stage 1'
    elif 140 <= systolic < 180 or 90 <= diastolic < 120:
        return 'Hypertension Stage 2'
    else:
        return 'Hypertensive Crisis'


if __name__ == '__main__':
    main()
