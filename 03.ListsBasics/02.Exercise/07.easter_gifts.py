gifts = input()
list_of_gifts = gifts.split()

while True:
    commands = input()
    if commands == 'No Money':
        break

    command_parts = commands.split()
    action = command_parts[0]

    if action == 'OutOfStock':
        gift = command_parts[1]
        list_of_gifts = ['None' if g == gift else g for g in list_of_gifts]

    elif action == 'Required':
        gift = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(list_of_gifts):
            list_of_gifts[index] = gift

    elif action == 'JustInCase':
        gift = command_parts[1]
        if list_of_gifts:
            list_of_gifts[-1] = gift

final_gifts = [gift for gift in list_of_gifts if gift != 'None']
print(" ".join(final_gifts))
