'''
Exercise: Coin Flip Simulation

This script simulates flipping a coin multiple times and calculates the
probability of heads and tails.

Usage:
    Call the function with number of flips.

Tags: for loop, random, simulations, probability
'''


import random


def main():
    '''Simulate coin flips and calculate probabilities.'''
    num_flips = 1000
    results = simulate_coin_flips(num_flips)

    # Using solution 1
    heads_count = results.count('H')
    tails_count = results.count('T')
    print(f'Heads: {heads_count}, Tails: {tails_count}')
    print(f'Probability of heads: {heads_count / num_flips:.3f}')
    print(f'Probability of tails: {tails_count / num_flips:.3f}')

    # Using solution 2
    heads, tails = simulate_coin_flips_2(num_flips)
    print(f'Heads: {heads}, Tails: {tails}')
    print(f'Probability of Heads: {heads / num_flips:.3f}')
    print(f'Probability of Tails: {tails / num_flips:.3f}')


def simulate_coin_flips(num_flips):
    '''
    Simulates flipping a coin multiple times.

    Parameters:
        num_flips (int): Number of coin flips.

    Returns:
        list: List of results ('H' for heads, 'T' for tails).
    '''
    results = []
    for _ in range(num_flips):
        result = random.choice(['H', 'T'])
        results.append(result)
    return results


def simulate_coin_flips_2(num_flips):
    '''
    Simulates flipping a coin multiple times.

    Parameters:
        num_flips (int): Number of coin flips.

    Returns:
        tuple: The number of heads and tails
    '''
    heads = 0
    tails = 0
    for _ in range(num_flips):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails


if __name__ == '__main__':
    main()
