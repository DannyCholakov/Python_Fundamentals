# Input: receive a sequence of numbers separated by space
numbers = input().split()

# Convert each number to float, get its absolute value, and store it in a list
absolute_values = [abs(float(num)) for num in numbers]

# Output the list of absolute values
print(absolute_values)
