'''
Exercise: Classifying Sound Levels

This script classifies sound levels in decibels (dB).

Sound level classification:
    - Very Quiet: < 30 dB
    - Quiet: 30 - 60 dB
    - Moderate: 60 - 90 dB
    - Loud: 90 - 120 dB
    - Very Loud: >= 120 dB

Usage:
    Call the function with the sound level in decibels.

Tags: if-elif-else, physics, sound levels
'''


def main():
    '''Classify sound levels.'''
    decibels = 938
    print(f'{decibels} dB is classified as {classify_sound(decibels)}.')


def classify_sound(decibels):
    '''
    Classifies sound levels in decibels.

    Parameters:
        decibels (int): The sound level in decibels.

    Returns:
        str: Classification of the sound level.
    '''
    if decibels < 30:
        return 'Very Quiet'
    elif 30 <= decibels < 60:
        return 'Quiet'
    elif 60 <= decibels < 90:
        return 'Moderate'
    elif 90 <= decibels < 120:
        return 'Loud'
    else:
        return 'Very Loud'


if __name__ == '__main__':
    main()
