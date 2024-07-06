'''
Exercise: Type of Projectile Motion

This script determines the type of projectile motion based on initial velocity
and angle of projection.

Types of projectile motion:
    - Horizontal: if the angle of projection is 0 degrees.
    - Vertical: if the angle of projection is 90 degrees.
    - Parabolic: if the angle of projection is between 0 and 90 degrees.

Usage:
    Call the function with initial velocity and launch angle.

Tags: if-elif-else, physics, projectile motion
'''


def main():
    '''Determine the type of projectile motion.'''
    velocity = 20
    angle = 90
    print(f'Motion of intitial velocity {velocity} m/s and launch '
          f'angle {angle}° is {classify_projectile_motion(velocity, angle)}')


def classify_projectile_motion(velocity, angle):
    '''
    Determines the type of projectile motion based on initial velocity and
    launch angle.

    Parameters:
        velocity (float): Initial velocity in m/s.
        angle (float): Launch angle in degrees.

    Returns:
        str: Projectile motion classification.
    '''
    if angle == 0 or angle == 90:
        return 'Vertical motion'
    elif angle > 0 and angle < 90:
        return 'Projectile motion'
    else:
        return 'Horizontal motion'


if __name__ == '__main__':
    main()
