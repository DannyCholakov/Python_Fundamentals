# Read input text and split into words
words = input().split()

# Use list comprehension to filter words with even length
even_length_words = [word for word in words if len(word) % 2 == 0]

# Print each word on a new line
for word in even_length_words:
    print(word)
