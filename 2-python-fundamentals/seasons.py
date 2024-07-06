'''
Exercise: Determining the Season

This script determines the season based on the month and day for both
northern and southern hemispheres.

Seasons classification for the Northern Hemisphere:
    - Winter: December 21 - March 19
    - Spring: March 20 - June 20
    - Summer: June 21 - September 21
    - Fall: September 22 - December 20

Seasons classification for the Southern Hemisphere:
    - Winter: June 21 - September 21
    - Spring: September 22 - December 20
    - Summer: December 21 - March 19
    - Fall: March 20 - June 20

Usage:
    Call the function with the month, day, and hemisphere.

Tags: if-elif-else, seasons, date
'''


def main():
    '''Determines the season based on the month and day.'''
    month = int(input('Enter the month (1-12): '))
    day = int(input('Enter the day (1-31): '))
    hemisphere = input('Enter the hemisphere (northern/southern): ').lower()
    season = get_season(month, day, hemisphere)
    print(f'The season is: {season}')


def get_season(month, day, hemisphere):
    '''
    Determine the season based on the month and day for the specified
    hemisphere.

    Parameters:
        month (int): The month of the year (1-12).
        day (int): The day of the month (1-31).
        hemisphere (str): The hemisphere ('northern' or 'southern').

    Returns:
        str: The season.
    '''
    if hemisphere == 'northern':
        if (month == 12 and day >= 21) or (1 <= month <= 2) or \
                (month == 3 and day < 21):
            return 'Winter'
        elif (month == 3 and day >= 21) or (4 <= month <= 5) or \
                (month == 6 and day < 21):
            return 'Spring'
        elif (month == 6 and day >= 21) or (7 <= month <= 8) or \
                (month == 9 and day < 21):
            return 'Summer'
        elif (month == 9 and day >= 21) or (10 <= month <= 11) or \
                (month == 12 and day < 21):
            return 'Autumn'
    elif hemisphere == 'southern':
        if (month == 6 and day >= 21) or (7 <= month <= 8) or \
                (month == 9 and day < 21):
            return 'Winter'
        elif (month == 9 and day >= 21) or (10 <= month <= 11) or \
                (month == 12 and day < 21):
            return 'Spring'
        elif (month == 12 and day >= 21) or (1 <= month <= 2) or \
                (month == 3 and day < 21):
            return 'Summer'
        elif (month == 3 and day >= 21) or (4 <= month <= 5) or \
                (month == 6 and day < 21):
            return 'Autumn'
    return 'Invalid date or hemisphere'


if __name__ == '__main__':
    main()
