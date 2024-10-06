def min_max_sum(sequence):
    # Convert the input string into a list of integers
    numbers = list(map(int, sequence.split()))

    # Calculate the minimum, maximum, and sum of the numbers
    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)

    # Return the results as a formatted string
    return minimum, maximum, total_sum


# Input: Read a sequence of numbers as a string
sequence = input()

# Get the min, max, and sum values
minimum, maximum, total_sum = min_max_sum(sequence)

# Output: Print the results
print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {total_sum}")
