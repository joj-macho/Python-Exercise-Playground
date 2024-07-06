'''
Exercise: Classifying Light Intensity

This script classifies the intensity of light based on its value in lumens.

Light intensity classification:
    Very Dim: < 100 lumens
    Dim: 100 - 300 lumens
    Moderate: 300 - 700 lumens
    Bright: 700 - 2000 lumens
    Very Bright: > 2000 lumens

Usage:
    Call the function with light intensity value.

Tags: if-elif-else, physics, light intensity
'''


def main():
    '''Classify light intensity.'''
    intensity = 500
    print(f'Light intensity of {intensity} lumens is '
          f'{classify_light_intensity(intensity)}')


def classify_light_intensity(intensity):
    '''
    Classifies the intensity of light based on its value in lumens.

    Parameters:
        intensity (int): Light intensity in lumens.

    Returns:
        str: Classification of light intensity.
    '''
    if intensity < 100:
        return 'Dim'
    elif 100 <= intensity < 500:
        return 'Normal'
    elif 500 <= intensity < 1000:
        return 'Bright'
    else:
        return 'Blinding'


if __name__ == '__main__':
    main()
