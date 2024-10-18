# Initial input for the journal
journal = input().split(', ')

while True:
    command = input()

    if command == "Craft!":
        break

    command_parts = command.split(' - ')
    action = command_parts[0]

    if action == "Collect":
        item = command_parts[1]
        if item not in journal:
            journal.append(item)

    elif action == "Drop":
        item = command_parts[1]
        if item in journal:
            journal.remove(item)

    elif action == "Combine Items":
        items = command_parts[1].split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index + 1, new_item)

    elif action == "Renew":
        item = command_parts[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)

# Final output after "Craft!" command
print(", ".join(journal))
