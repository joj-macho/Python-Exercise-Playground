'''
Exercise: Election Voting Eligibility

This script determines if a person is eligible to vote based on their age and
citizenship status.

Usage:
    Call the function with age and citizenship values.

Tags: if-else, voting, eligibility
'''


def main():
    '''Determine voting eligibility.'''
    age = int(input('Enter your age: '))
    citizenship = input('Enter your citizenship status '
                        '(citizen, non-citizen): ').lower()
    eligibility = is_eligible_to_vote(age, citizenship)
    if eligibility:
        print('You are eligible to vote.')
    else:
        print('You are not eligible to vote.')


def is_eligible_to_vote(age, citizenship):
    '''
    Determine if a person is eligible to vote.

    Parameters:
        age (int): The age of the person.
        citizenship (str): The citizenship status (citizen, non-citizen).

    Returns:
        bool: True if eligible, False otherwise.
    '''
    if age >= 18 and citizenship == 'citizen':
        return True
    else:
        return False


if __name__ == '__main__':
    main()
