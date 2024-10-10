# Step 1: Initialize the train with the given number of wagons
number_of_wagons = int(input())
train = [0] * number_of_wagons

# Step 2: Process commands
while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "add":
        people = int(command_parts[1])
        train[-1] += people  # Add people to the last wagon

    elif action == "insert":
        index = int(command_parts[1])
        people = int(command_parts[2])
        train[index] += people  # Insert people at the given index

    elif action == "leave":
        index = int(command_parts[1])
        people = int(command_parts[2])
        train[index] -= people  # Remove people from the given index

# Step 3: Print the final state of the train
print(train)
