'''
Exercise: Final Price with Discount

This script calculates the final price of an item after applying a discount.

Formula:
    final_price = original_price * (1 - discount_rate / 100)

Usage:
    Call the main function and follow the prompts.

Tags: arithmetic operations, discount, final price, calculations
'''


def main():
    '''Calculate final price after discount from user input.'''
    original_price = float(input('Enter the original price: '))
    discount_percentage = float(input('Enter the discount percentage: '))

    final_price = calculate_final_price(original_price, discount_percentage)
    print(f'The final price after {discount_percentage}% discount is '
          f'{final_price:.2f}')


def calculate_final_price(original_price, discount_percentage):
    '''
    Calculates the final price after applying the discount.

    Parameters:
        original_price (float): The original price of an item.
        discount_percentage (float): The discount percentage of an item.

    Returns:
        float: The final price of an item after discount.
    '''
    discount_amount = (discount_percentage / 100) * original_price
    return original_price - discount_amount


if __name__ == '__main__':
    main()
