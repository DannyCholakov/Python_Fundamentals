def pokemon_dont_go():
    # Read the initial sequence of distances
    distances = list(map(int, input().split()))
    total_removed = 0  # To keep track of the total sum of removed elements

    while distances:
        index = int(input())  # Read the index

        # Determine which element to remove
        if index < 0:
            removed_element = distances[0]
            distances[0] = distances[-1]  # Replace the first element with the last
        elif index >= len(distances):
            removed_element = distances[-1]
            distances[-1] = distances[0]  # Replace the last element with the first
        else:
            removed_element = distances[index]
            del distances[index]  # Remove the element at the specified index

        # Increment the total of removed elements
        total_removed += removed_element

        # Update the distances based on the removed element
        for i in range(len(distances)):
            if distances[i] <= removed_element:
                distances[i] += removed_element  # Increase
            else:
                distances[i] -= removed_element  # Decrease

    # Output the total of removed elements
    print(total_removed)


# Example usage:
pokemon_dont_go()
