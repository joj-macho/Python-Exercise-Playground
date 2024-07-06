'''
Exercise: Direction of a Chemical Reaction at Equilibrium

This script determines the direction of a chemical reaction at equilibrium
based on the reaction quotient (Q) and the equilibrium constant (K).

Reaction direction classification:
    Q < K: The reaction proceeds in the forward direction.
    Q = K: The reaction is at equilibrium.
    Q > K: The reaction proceeds in the reverse direction.

Usage:
    Call the function with the reaction quotient and equilibrium constant.

Tags: if-elif-else, chemistry, chemical equilibrium
'''


def main():
    '''Determine the direction of a chemical reaction.'''
    Q = float(input('Enter the reaction quotient (Q): '))
    K = float(input('Enter the equilibrium constant (K): '))
    direction = determine_equilibrium_direction(Q, K)
    print(f'The reaction is proceeding in the {direction} direction.')


def determine_equilibrium_direction(Q, K):
    '''
    Determine the direction of a chemical reaction at equilibrium.

    Parameters:
        Q (float): The reaction quotient.
        K (float): The equilibrium constant.

    Returns:
        str: The direction of the reaction (forward, reverse, at equilibrium).
    '''
    if Q < K:
        return 'Forward'
    elif Q > K:
        return 'Reverse'
    else:
        return 'At Equilibrium'


if __name__ == '__main__':
    main()
