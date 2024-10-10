# Step 1: Read the input words and the target palindrome
words = input().split()  # Split the first input into a list of words
target_palindrome = input()  # The palindrome to search for

# Step 2: Initialize an empty list to store found palindromes
found_palindromes = []

# Step 3: Iterate over the words and check if each is a palindrome
for word in words:
    if word == word[::-1]:  # Check if the word is the same forward and backward
        found_palindromes.append(word)  # If it's a palindrome, add it to the list

# Step 4: Count the occurrences of the target palindrome in the list
palindrome_count = found_palindromes.count(target_palindrome)

# Step 5: Print the results
print(found_palindromes)
print(f"Found palindrome {palindrome_count} times")
