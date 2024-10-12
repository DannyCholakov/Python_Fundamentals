def group_of_tens(numbers_str):
    # Convert input string into a list of integers
    numbers = list(map(int, numbers_str.split(", ")))

    group = 10  # Starting group boundary
    while numbers:  # Continue until no numbers are left
        # Get the numbers that fall into the current group (<= group)
        current_group = [num for num in numbers if num <= group]

        # Print the current group
        print(f"Group of {group}'s: {current_group}")

        # Remove the numbers that are already grouped
        numbers = [num for num in numbers if num > group]

        # Move to the next group boundary
        group += 10

group_of_tens(input())
