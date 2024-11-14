import re

all_numbers = []

while True:
    line = input()
    if line == "":
        break

    numbers = re.findall(r'\d+', line)
    all_numbers.extend(numbers)

print(" ".join(all_numbers))
