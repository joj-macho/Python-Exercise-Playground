'''
Exercise: Simple and Compount Interest

This script calculates the simple and compound interest using the formulae:
S.I = PRT/100
C.I = P(1 + R/n)^(nT) - P

Usage:
    Call the functions with the principal amount, interest rate, and time.

Tags: arithmetic operations, simple interest, compound interest, finance
'''


def main():
    '''Main function to demonstrate simple and compound interest.'''
    principal, rate, time, n = 1000, 5, 2, 2

    s_interest = simple_interest(principal, rate, time)
    print(f'Simple Interest = {s_interest:.2f}')
    print(f'Simple Interest total amount: {principal + s_interest}')

    c_interest = compound_interest(principal, rate, time, n)
    print(f'Compound Interest: {c_interest:.2f}')
    print(f'Compound Interest total amount: {principal + c_interest}')


def simple_interest(principal, rate, time):
    '''
    Calculates the simple interest.

    Parameters:
        principal (int/float): The principal amount.
        rate (int/float): The interest rate.
        time (int/float): The time period.

    Returns:
        float: The simple interest.
    '''
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, n):
    '''
    Calculates the compound interest.

    Parameters:
        principal (int/float): The principal amount.
        rate (int/float): The interest rate.
        time (int/float): The time period.
        n (int): Number of times interest is compounded in a year.
    Returns:
        float: The compound interest.
    '''
    return principal * (1 + rate / (n * 100)) ** (n * time) - principal


if __name__ == '__main__':
    main()
