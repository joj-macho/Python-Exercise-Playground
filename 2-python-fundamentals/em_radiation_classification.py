'''
Exercise: Electromagnetic Spectrum

This script classifies electromagnetic radiation based on wavelength.

Electromagnetic spectrum classification:
    - Radio waves: > 1 m
    - Microwaves: 1 mm to 1 m
    - Infrared: 700 nm to 1 mm
    - Visible light: 400 nm to 700 nm
    - Ultraviolet: 10 nm to 400 nm
    - X-rays: 0.01 nm to 10 nm
    - Gamma rays: < 0.01 nm

Usage:
    Call the function with wavelength value.

Tags: if-elif-else, physics, electromagnetic spectrum
'''


def main():
    '''Classify EM radiation.'''
    wavelength = 1e-6
    print(f'Electromagnetic radiation of {wavelength} meters '
          f'is {classify_em_radiation(wavelength)}.')


def classify_em_radiation(wavelength):
    '''
    Classifies electromagnetic radiation based on wavelength.

    Parameters:
        wavelength (float): Wavelength in meters.

    Returns:
        str: Classification of electromagnetic radiation.
    '''
    if wavelength > 1e-1:
        return 'Radio waves'
    elif 1e-1 >= wavelength > 1e-3:
        return 'Microwaves'
    elif 1e-3 >= wavelength > 7e-7:
        return 'Infrared'
    elif 7e-7 >= wavelength > 4e-7:
        return 'Visible light'
    elif 4e-7 >= wavelength > 1e-8:
        return 'Ultraviolet'
    elif 1e-8 >= wavelength > 1e-11:
        return 'X-rays'
    else:
        return 'Gamma rays'


if __name__ == '__main__':
    main()
