'''
Exercise: Traffic Light Action

This script determines whether to stop, slow down, or go based on the color
of a traffic light.

Usage:
    Call the function with traffic light colors.

Tags: if-elif-else, traffic light, classification
'''


def main():
    '''Classify the traffic light action based on color.'''
    color = input('Enter the traffic light color '
                  '(red, yellow, green): ').lower()
    action = traffic_light_action(color)
    print(f'The color {color} action to take is: {action}')


def traffic_light_action(color):
    '''
    Determine action based on traffic light color.

    Parameters:
        color (str): The color of the traffic light.

    Returns:
        str: The action to take.
    '''
    if color == 'red':
        return 'Stop'
    elif color == 'yellow':
        return 'Slow Down'
    elif color == 'green':
        return 'Go'
    else:
        return 'Invalid color'


if __name__ == '__main__':
    main()
