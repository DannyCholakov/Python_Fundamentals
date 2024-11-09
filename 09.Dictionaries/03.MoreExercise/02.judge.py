contests = {}
individual_scores = {}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username in contests[contest]:
        if contests[contest][username] < points:
            individual_scores[username] += (points - contests[contest][username])
            contests[contest][username] = points
    else:
        contests[contest][username] = points
        if username not in individual_scores:
            individual_scores[username] = 0
        individual_scores[username] += points

for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for idx, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{idx}. {username} <::> {points}")

print("Individual standings:")
sorted_individuals = sorted(individual_scores.items(), key=lambda x: (-x[1], x[0]))
for idx, (username, points) in enumerate(sorted_individuals, start=1):
    print(f"{idx}. {username} -> {points}")
