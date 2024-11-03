# Initialize the phonebook dictionary
phonebook = {}

# Collect input for the phonebook
while True:
    entry = input()
    if entry.isdigit():  # If the entry is a number, break and store N
        N = int(entry)
        break
    name, number = entry.split("-")
    phonebook[name] = number  # Update the number if the name already exists

# Perform N searches for contacts
for _ in range(N):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
