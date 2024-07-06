'''
Exercise: Classifying pH Level

This script classifies a solution based on its pH level.

pH level classification:
    - Acidic: pH < 7
    - Neutral: pH = 7
    - Basic: pH > 7

Usage:
    Call the function with a pH value.

Tags: if-elif-else, chemistry, pH level
'''


def main():
    '''Classify the pH level of a solution.'''
    ph = 7
    print(f'The solution is {classify_ph(ph)}')


def classify_ph(ph):
    '''
    Classifies a solution based on its pH level.

    Parameters:
        ph (float): pH value.

    Returns:
        str: Classification.
    '''
    if ph < 7:
        return 'Acidic'
    elif ph == 7:
        return 'Neutral'
    else:
        return 'Basic'


if __name__ == '__main__':
    main()
