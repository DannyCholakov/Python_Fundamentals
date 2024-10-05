def characters_in_range(char1, char2):
    # Get ASCII values of the input characters
    start = ord(char1)
    end = ord(char2)

    # Ensure the start is always smaller
    if start > end:
        start, end = end, start

    # Create a list of characters in the range
    result = [chr(i) for i in range(start + 1, end)]

    # Join the list into a string separated by a single space
    return ' '.join(result)


# Input: Reading two characters from the console
char1 = input()
char2 = input()

# Output: Print the characters between the two input characters
print(characters_in_range(char1, char2))
