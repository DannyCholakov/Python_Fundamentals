# Parse the input and battlefield grid
n = int(input())  # Number of rows
battlefield = [list(map(int, input().split())) for _ in range(n)]  # Matrix representing the battlefield

# Get the attack coordinates
attacks = input().split()  # List of attacks in "row-col" format

destroyed_ships = 0  # Counter for destroyed ships

# Process each attack
for attack in attacks:
    row, col = map(int, attack.split('-'))  # Parse the attack coordinates

    # Check if there's a ship at the attacked position
    if battlefield[row][col] > 0:
        # Decrease the ship's health
        battlefield[row][col] -= 1

        # If the ship's health becomes 0, it's destroyed
        if battlefield[row][col] == 0:
            destroyed_ships += 1

# Output the total number of destroyed ships
print(destroyed_ships)
