# Step 1: Initialize an empty list to store the notes with their importance
to_do_list = []

# Step 2: Process each input
while True:
    command = input()

    if command == "End":
        break

    # Split the input into importance and note
    importance, note = command.split("-")
    importance = int(importance)  # Convert importance to integer

    # Step 3: Insert each note with its importance into the list
    to_do_list.append((importance, note))

# Step 4: Sort the to-do list by importance
to_do_list.sort(key=lambda x: x[0])

# Step 5: Extract and print the notes, sorted by importance
sorted_notes = [note for _, note in to_do_list]
print(sorted_notes)
