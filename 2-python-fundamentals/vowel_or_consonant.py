'''
Exercise: Vowel or Consonant

This script checks if a given character is a vowel or a consonant.

Vowels: 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase)
Consonants: All other alphabetic characters.

Usage:
    Call the function with the character.

Tags: if-else, string, character classification
'''


def main():
    '''Determine if a character is a vowel or consonant.'''
    char = 'a'
    print(f'{char} is a {vowel_or_consonant(char)}.')


def vowel_or_consonant(char):
    '''
    Determines if a character is a vowel or consonant.

    Parameters:
        char (str): The character to check.

    Returns:
        str: 'vowel' if the character is a vowel, 'consonant' otherwise.
    '''
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return 'vowel'
    else:
        return 'consonant'


if __name__ == '__main__':
    main()
