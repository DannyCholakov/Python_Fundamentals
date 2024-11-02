# Read the input and split it into words
words = input().split()

# Create a dictionary to count the occurrences of each word (case-insensitive)
word_counts = {}

for word in words:
    word_lower = word.lower()
    if word_lower in word_counts:
        word_counts[word_lower] += 1
    else:
        word_counts[word_lower] = 1

# Collect words that occur an odd number of times
result = [word for word, count in word_counts.items() if count % 2 != 0]

# Print the result elements in lowercase, in their order of appearance
print(" ".join(result))
