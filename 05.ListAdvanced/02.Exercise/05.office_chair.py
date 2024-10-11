# Number of rooms
n = int(input())

# Initialize variables to track the total number of free chairs and any deficit
total_free_chairs = 0
enough_chairs = True

# Iterate over each room
for room_number in range(1, n + 1):
    # Read the input and split the number of chairs and visitors
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])

    # Check if the room has enough chairs
    if chairs >= visitors:
        total_free_chairs += chairs - visitors
    else:
        # If not enough chairs, calculate how many more are needed
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room_number}")
        enough_chairs = False

# If all rooms have enough chairs, print the total free chairs
if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
