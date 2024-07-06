'''
Exercise: Wavelengths of Visible Light

This script classifies the color of light based on its wavelength in
nanometers.

Light color classification based on wavelength:
    - Violet: 380 - 450 nm
    - Blue: 450 - 495 nm
    - Green: 495 - 570 nm
    - Yellow: 570 - 590 nm
    - Orange: 590 - 620 nm
    - Red: 620 - 750 nm

Usage:
    Call the function with a wavelength value.

Tags: if-elif-else, physics, light color, wavelength
'''


def main():
    '''Classify the color of light based on its wavelength.'''
    wavelength = 500
    print(f'The color of light of wavelength {wavelength} nm is '
          f'{classify_color(wavelength)}')


def classify_color(wavelength):
    '''
    Classifies the color of light based on its wavelength.

    Parameters:
        wavelength (int): Wavelength in nanometers.

    Returns:
        str: Color of light.
    '''
    if 380 <= wavelength < 450:
        return 'Violet'
    elif 450 <= wavelength < 495:
        return 'Blue'
    elif 495 <= wavelength < 570:
        return 'Green'
    elif 570 <= wavelength < 590:
        return 'Yellow'
    elif 590 <= wavelength < 620:
        return 'Orange'
    elif 620 <= wavelength <= 750:
        return 'Red'
    else:
        return 'Outside visible spectrum'


if __name__ == '__main__':
    main()
