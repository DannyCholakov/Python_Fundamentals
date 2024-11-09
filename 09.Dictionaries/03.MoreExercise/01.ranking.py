contests = {}
users = {}

while True:
    command = input()
    if command == "end of contests":
        break

    contest, password = command.split(":")
    contests[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break

    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username] or users[username][contest] < points:
            users[username][contest] = points

best_user = ""
best_points = 0

for user, contests_data in users.items():
    total_points = sum(contests_data.values())
    if total_points > best_points:
        best_user = user
        best_points = total_points

print(f"Best candidate is {best_user} with total {best_points} points.")

print("Ranking:")
for user in sorted(users.keys()):
    print(user)
    for contest, points in sorted(users[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
