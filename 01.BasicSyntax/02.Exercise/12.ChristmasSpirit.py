quantity_per_shopping = int(input())
days = int(input())

cost = 0
points = 0

ornament_set_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

quantity = quantity_per_shopping

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        cost += quantity * ornament_set_price
        points += 5

    if day % 3 == 0:
        cost += quantity * (tree_skirt+tree_garland)
        points += 3 + 10

    if day % 5 == 0:
        cost += quantity * tree_lights
        points += 17

        if day % 3 == 0:
            points += 30

    if day % 10 == 0:
        points -= 20
        cost += (tree_skirt+tree_garland+tree_lights)

    if day == days and day % 10 == 0:
        points -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {points}')
