number_of_cities = int(input())

day = 0
total_profit = 0.0

for city in range(number_of_cities):
    day += 1

    name_of_city = input()
    owners_income = float(input())
    owners_expenses = float(input())

    if day % 3 == 0:
        if day % 5 == 0:
            owners_income *= 0.90
            daily_income = owners_income-owners_expenses
        else:
            owners_expenses *= 1.50
            daily_income = owners_income - owners_expenses
    elif day % 5 == 0:
        owners_income *= 0.90
        daily_income = owners_income - owners_expenses
    else:
        daily_income = owners_income - owners_expenses

    total_profit += daily_income
    print(f"In {name_of_city} Burger Bus earned {daily_income:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

