# Read the number of word-synonym pairs
n = int(input())

# Initialize the dictionary to store synonyms
synonyms = {}

# Loop to read words and synonyms
for _ in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []  # Initialize an empty list if the word is not in the dictionary

    synonyms[word].append(synonym)  # Add the synonym to the list

# Print each word and its synonyms
for word, synonym_list in synonyms.items():
    print(f"{word} - {', '.join(synonym_list)}")
