import re


participants = input().split(", ")

distances = {name: 0 for name in participants}

name_pattern = r'[A-Za-z]'
distance_pattern = r'\d'

while True:
    try:
        line = input()
        if line.strip() == "end of race":
            break

        name_chars = re.findall(name_pattern, line)
        name = "".join(name_chars)

        distance_digits = re.findall(distance_pattern, line)
        distance = sum(int(digit) for digit in distance_digits)

        if name in distances:
            distances[name] += distance

    except EOFError:
        break

sorted_participants = sorted(distances.items(), key=lambda x: x[1], reverse=True)

places = ["1st place: {}", "2nd place: {}", "3rd place: {}"]
for i in range(min(3, len(sorted_participants))):
    print(places[i].format(sorted_participants[i][0]))
