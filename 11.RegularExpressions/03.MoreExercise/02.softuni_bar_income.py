import re

total_income = 0

pattern = r'%([A-Z][a-z]+)%<([\w]+)>\|(\d+)\|(\d+(?:\.\d+)?)\$'

while True:
    line = input()
    if line.strip() == "end of shift":
        break

    match = re.search(pattern, line)
    if match:
        customer = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        total_price = count * price
        total_income += total_price

        print(f"{customer}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")
