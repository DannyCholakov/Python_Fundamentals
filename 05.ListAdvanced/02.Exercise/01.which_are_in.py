# Read input and split by ", "
first_sequence = input().split(", ")
second_sequence = input().split(", ")

# List to store the matching substrings
result = []

# Loop through each string in the first sequence
for first_str in first_sequence:
    # Check if first_str is a substring of any string in second_sequence
    if any(first_str in second_str for second_str in second_sequence):
        result.append(first_str)

# Print the result list
print(result)
