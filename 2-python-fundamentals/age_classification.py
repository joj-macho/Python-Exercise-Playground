'''
Exercise: Age Classification

This script classifies a person as a child, teenager, adult, or senior
based on their age.

Usage:
    Call the function with age value.

Tags: if-elif-else, age classification
'''


def main():
    '''Classify the user age.'''
    age = 19
    classification = classify_age(age)
    print(f'Age {age} is classified as: {classification}')


def classify_age(age):
    '''
    Classify a person's age.

    Parameters:
        age (int): The age of the person.

    Returns:
        str: The age classification (child, teenager, adult, senior).
    '''
    if age < 13:
        return 'Child'
    elif age < 20:
        return 'Teenager'
    elif age < 65:
        return 'Adult'
    else:
        return 'Senior'


if __name__ == '__main__':
    main()
