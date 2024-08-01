'''
Exercise: 99 Bottles of Beer Lyrics

This script displays the lyrics of the "99 Bottles of Beer" song.

- print_lyrics_1(): Uses a straightforward loop with if-else for singular and
plural handling.
- print_lyrics_2(): Uses a ternary operator within the formatted string for
concise singular and plural handling.

Usage:
    Call the function to display the lyrics.

Tags: for loop, iterations, string manipulation
'''


def main():
    '''Display the lyrics of the "99 Bottles of Beer" song.'''
    print_lyrics_2()


def print_lyrics_1():
    '''Displays the lyrics of the "99 Bottles of Beer" song.'''
    # From 99 bottles to 2 bottles
    for num_of_bottles in range(99, 1, -1):
        print(f'{num_of_bottles} bottles of beer on the wall,')
        print(f'{num_of_bottles} bottles of beer,')
        print('Take one down, pass it around,')

        # When 1 beer is left: bottles --> bottle
        if (num_of_bottles - 1) == 1:
            print('1 bottle of beer on the wall,')
        else:
            print(f'{num_of_bottles -1} bottles of beer on the wall,')

    # Last stanza
    print('1 bottle of beer on the wall,')
    print('1 bottle of beer,')
    print('Take one down, pass it around,')
    print('No more bottles of beer on the wall!')


def print_lyrics_2():
    '''Displays the lyrics of the "99 Bottles of Beer" song.'''
    for i in range(99, 0, -1):
        print(f'{i} bottle{"s" if i > 1 else ""} of beer on the wall,')
        print(f'{i} bottle{"s" if i > 1 else ""} of beer,')
        print('Take one down, pass it around,')
        print(f'{i - 1 if (i - 1) > 0 else "no more"} '
              f'bottlzze{"s" if i > 1 else ""} of beer on the wall.')
        print()


if __name__ == '__main__':
    main()
