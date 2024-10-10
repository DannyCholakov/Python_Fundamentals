# Step 1: Read the input string and split it into a list of names
names = input().split(", ")

# Step 2: Sort the names by their length (descending), and alphabetically for names with the same length
sorted_names = sorted(names, key=lambda x: (-len(x), x))

# Step 3: Print the result
print(sorted_names)
