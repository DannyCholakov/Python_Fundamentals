orders = int(input())
totalPrice = 0.00
for i in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules_perDay = int(input())

    if not (0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= capsules_perDay <= 2000):
        continue

    order_price = capsule_price * capsules_perDay * days
    print(f'The price for the coffee is: ${order_price:.2f}')
    totalPrice += order_price

print(f'Total: ${totalPrice:.2f}')