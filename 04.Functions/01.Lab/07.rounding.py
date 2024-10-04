def round_numbers(numbers):
    # Convert each number to a float, round it, and return the list
    return [round(float(num)) for num in numbers.split()]

# Input: receive the numbers as a string
numbers = input()

# Output: print the list of rounded numbers
print(round_numbers(numbers))
