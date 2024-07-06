'''
Exercise: Richter Scale

This script classifies earthquake magnitude based on the Richter scale.

Earthquake magnitude classification:
    - Micro: < 2.0
    - Minor: 2.0 - 3.9
    - Light: 4.0 - 4.9
    - Moderate: 5.0 - 5.9
    - Strong: 6.0 - 6.9
    - Major: 7.0 - 7.9
    - Great: >= 8.0

Usage:
    Call the function with a magnitude value.

Tags: if-elif-else, geology, earthquake, Richter scale
'''


def main():
    '''Classify earthquake magnitude.'''
    magnitude = 6.5
    print(f'The earthquake of magnitude {magnitude} is classified as '
          f'{classify_earthquake(magnitude)}')


def classify_earthquake(magnitude):
    '''
    Classifies earthquake magnitude based on the Richter scale.

    Parameters:
        magnitude (float): Magnitude of the earthquake.

    Returns:
        str: Earthquake classification.
    '''
    if magnitude < 2.0:
        return 'Micro'
    elif 2.0 <= magnitude < 4.0:
        return 'Minor'
    elif 4.0 <= magnitude < 6.0:
        return 'Light'
    elif 6.0 <= magnitude < 7.0:
        return 'Moderate'
    elif 7.0 <= magnitude < 8.0:
        return 'Strong'
    elif 8.0 <= magnitude < 10.0:
        return 'Major'
    else:
        return 'Great'


if __name__ == '__main__':
    main()
