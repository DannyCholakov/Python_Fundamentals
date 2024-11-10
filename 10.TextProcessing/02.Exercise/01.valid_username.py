def is_valid_username(username):
    if len(username) < 3 or len(username) > 16:
        return False

    for char in username:
        if not (char.isalnum() or char in '-_'):
            return False

    return True

usernames = input().split(", ")

for username in usernames:
    if is_valid_username(username):
        print(username)
