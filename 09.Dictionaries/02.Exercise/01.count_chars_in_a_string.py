# Read the input string
text = input()

# Create a dictionary to count character occurrences
char_count = {}

for char in text:
    if char != " ":  # Ignore spaces
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Print the character counts in the specified format
for char, count in char_count.items():
    print(f"{char} -> {count}")
