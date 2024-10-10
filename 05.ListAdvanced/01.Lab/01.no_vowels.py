def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # List comprehension to filter out vowels
    result = ''.join([char for char in text if char not in vowels])
    return result

# Input
text = input()

# Call the function and print the result
print(remove_vowels(text))
