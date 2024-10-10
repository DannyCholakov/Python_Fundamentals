# Step 1: Read the input string and convert it into a list of integers
numbers = list(map(int, input().split(", ")))

# Step 2: Find the indices of the even numbers
even_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]

# Step 3: Print the result
print(even_indices)
