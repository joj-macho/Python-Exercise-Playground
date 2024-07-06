'''
Exercise: Dog Years

This script converts human years to dog years.

Dogs age differently than humans, typically aging faster in their
early years. This script uses a simplified conversion where:
- The first two years of a dog's life count as 10.5 years each.
- Each subsequent year counts as 4 years.

Usage:
    Call the function with the human years value.

Tags: arithmetic operations, if-else, age conversion
'''

def main():
    '''Convert human years to dog years.'''
    human_years = int(input('Enter human age: '))
    print(f'The age {human_years} years in dog years is '
          f'{calculate_dog_years(human_years)} years')


def calculate_dog_years(human_years):
    '''
    Converts human years to dog years.

    Parameters:
        human_years (int): Age in human years.

    Returns:
        int: Age in dog years.
    '''
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4


if __name__ == '__main__':
    main()
