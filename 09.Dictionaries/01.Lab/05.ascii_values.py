# Input: list of characters separated by ", "
characters = input().split(", ")

# Create a dictionary using comprehension
ascii_dict = {char: ord(char) for char in characters}

# Output the result
print(ascii_dict)
