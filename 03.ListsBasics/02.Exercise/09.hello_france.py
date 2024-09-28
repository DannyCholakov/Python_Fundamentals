items = input().split('|')
budget = float(input())

max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

bought_items = []
total_spent = 0

for item in items:
    item_type, price = item.split('->')
    price = float(price)

    if price <= max_prices.get(item_type, 0) and price <= budget:
        bought_items.append(price)
        budget -= price
        total_spent += price

new_prices = [price * 1.40 for price in bought_items]

profit = sum(new_prices) - total_spent
budget += sum(new_prices)

print(" ".join(f"{price:.2f}" for price in new_prices))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
