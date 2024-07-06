'''
Exercise: Speed Classification

This script classifies the speed of an object based on its value.

Speed classification:
    - Stationary: 0 m/s
    - Slow: 0 < speed <= 5 m/s
    - Average: 5 < speed <= 15 m/s
    - High Speed: 15 < speed <= 100 m/s
    - Subsonic: speed < 343 m/s
    - Transonic: 343 <= speed < 1235 m/s
    - Supersonic: 1235 <= speed < 6174 m/s
    - Hypersonic: speed > 6174 m/s

Usage:
    Call the function with a speed value in m/s.

Tags: if-elif-else, physics, speed
'''


def main():
    '''Classify the speed of an object.'''
    speed = 98
    print(f'The object moving at {speed} m/s is {classify_speed(speed)} speed')


def classify_speed(speed):
    '''
    Classifies the speed of an object.

    Parameters:
        speed (float): Speed in m/s.

    Returns:
        str: Speed classification.
    '''
    if speed == 0:
        return 'Stationary'
    elif 5 < speed <= 15:
        return 'Slow'
    elif 15 < speed <= 100:
        return 'Very Fast'
    elif speed < 343:
        return 'Subsonic'
    elif 343 <= speed < 1235:
        return 'Transonic'
    elif 1235 <= speed < 6174:
        return 'Supersonic'
    else:
        return 'Hypersonic'


if __name__ == '__main__':
    main()
