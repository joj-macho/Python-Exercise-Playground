'''
Exercise: Every 15 Minutes

This script displays the time for every 15-minute interval in a 24-hour day.

Usage:
    Call the function to display the times.

Tags: for loop, nested for loop, time, intervals
'''


def main():
    '''Display the time in 15-minute intervals.'''
    display_intervals_2()


def display_intervals_1():
    '''Displays the time for every 15-minute intervals.'''
    for hour in range(24):
        for minute in range(0, 60, 15):
            print(f'{hour:02}:{minute:02}')


def display_intervals_2():
    '''Displays the time for every 15-minute intervals.'''
    # Include am and pm
    for meridiem in ('am', 'pm'):
        for hour in ('12', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9', '10', '11'):
            for minute in range(0, 60, 15):
                print(f'{hour}:{minute:02} {meridiem}')


if __name__ == '__main__':
    main()
