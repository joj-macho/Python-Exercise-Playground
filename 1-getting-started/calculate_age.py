'''
Exercise: Calculate Age

This script demonstrates how to calculate a person's age given their
birthdate using the datetime module.

Usage:
    Call the main function to calculate and print age.

Tags: datetime module, calculate age, date operations
'''

import datetime


def main():
    '''Calculates and prints age given a birthdate.'''
    birthdate = datetime.date(1990, 1, 1)
    age = calculate_age(birthdate)

    print('Age:', age)


def calculate_age(birthdate):
    '''Calculates age based on the birthdate.'''
    today = datetime.date.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age


if __name__ == '__main__':
    main()
