import re

furniture_list = []

total_cost = 0

pattern = r'>>([a-zA-Z\s]+)<<(\d+(\.\d+)?)!(\d+)'

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)
    if match:
        furniture_name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(4))

        furniture_list.append(furniture_name)
        total_cost += price * quantity

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
