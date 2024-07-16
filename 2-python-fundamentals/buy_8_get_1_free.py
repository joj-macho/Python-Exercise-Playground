'''
Exercise: Buy 8 Get 1 Free

This script calculates the total cost of items where a "Buy 8, Get 1 Free"
offer is applied.

Usage:
    Call the function with the number of coffees ordered and the price per
    coffee.

Tags: while loop, if-else, arithmetic operations, sales calculations
'''


def main():
    '''Demonstrate coffee order calculation.'''
    num_coffees = 16
    price_per_coffee = 5
    print(f'Total Cost: '
          f'${calculate_total_cost_2(num_coffees, price_per_coffee)}')


def calculate_total_cost_1(num_coffees, price_per_coffee):
    '''
    Calculate the total cost of a coffee order with "buy 8 get 1 free" offer.

    Parameters:
        num_coffees (int): The number of coffees ordered.
        price_per_coffee (int/float): The price of each coffee.

    Returns:
        int/float: The total cost of the order.
    '''
    paid_coffees = 0
    remaining_coffees = num_coffees

    while remaining_coffees > 0:
        # If there are at least 9 coffees, 8 are paid and 1 is free
        if remaining_coffees >= 9:
            paid_coffees += 8
            remaining_coffees -= 9
        else:
            paid_coffees += remaining_coffees
            remaining_coffees = 0

    # Calculate total cost
    total_cost = paid_coffees * price_per_coffee

    return total_cost


def calculate_total_cost_2(num_coffees, price_per_coffee):
    '''
    Calculate the total cost of a coffee order with "buy 8 get 1 free" offer.

    Parameters:
        num_coffees (int): The number of coffees ordered.
        price_per_coffee (int/float): The price of each coffee.

    Returns:
        int/float: The total cost of the order.
    '''
    # Number of free coffess
    free_coffees = num_coffees // 9

    # Number of paid coffees
    paid_coffees = num_coffees - free_coffees

    return paid_coffees * price_per_coffee


if __name__ == '__main__':
    main()
