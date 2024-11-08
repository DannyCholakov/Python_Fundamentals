submissions = {}
user_scores = {}

while True:
    command = input()
    if command == "exam finished":
        break

    parts = command.split("-")

    if parts[1] == "banned":
        username = parts[0]
        if username in user_scores:
            del user_scores[username]
    else:
        username, language, points = parts[0], parts[1], int(parts[2])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        if username not in user_scores:
            user_scores[username] = {}
        if language not in user_scores[username]:
            user_scores[username][language] = points
        else:
            user_scores[username][language] = max(user_scores[username][language], points)

print("Results:")
for username, languages in user_scores.items():
    for language, points in languages.items():
        print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
