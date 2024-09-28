
fires = input().split("#")
water = int(input())

valid_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

total_effort = 0.0
total_fire = 0
extinguished_cells = []

for fire in fires:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if value in valid_ranges[fire_type] and water >= value:
        water -= value
        total_fire += value
        effort = value * 0.25
        total_effort += effort
        extinguished_cells.append(value)

print("Cells:")
for cell in extinguished_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
