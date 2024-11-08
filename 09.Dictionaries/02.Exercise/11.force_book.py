force_sides = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")

        user_exists = any(force_user in users for users in force_sides.values())

        if not user_exists:
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        for side, users in force_sides.items():
            if force_user in users:
                users.remove(force_user)
                break

        if force_side not in force_sides:
            force_sides[force_side] = []
        force_sides[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for side, users in force_sides.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
