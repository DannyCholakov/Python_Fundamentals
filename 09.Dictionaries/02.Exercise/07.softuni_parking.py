commands_number = int(input())

user_dictionary = {}

for command in range(commands_number):
    command_parts = input().split()
    action = command_parts[0]
    username = command_parts[1]

    if action == "register":
        license_plate = command_parts[2]
        if username in user_dictionary:
            print(f"ERROR: already registered with plate number {user_dictionary[username]}")
        else:
            user_dictionary[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif action == "unregister":
        if username in user_dictionary:
            del user_dictionary[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate in user_dictionary.items():
    print(f"{username} => {license_plate}")
