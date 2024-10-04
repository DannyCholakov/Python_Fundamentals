def calculate_total(product, quantity):
    # Define product prices
    prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }

    # Calculate total price
    total_price = prices[product] * quantity

    # Return the result formatted to 2 decimal places
    return f'{total_price:.2f}'


# Input: receive the product and quantity from the user
product = input()
quantity = int(input())

# Output: Print the total price
print(calculate_total(product, quantity))
