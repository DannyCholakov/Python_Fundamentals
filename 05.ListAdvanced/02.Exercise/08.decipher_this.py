def decipher_this(message):
    deciphered_words = []

    # Split the message into words
    words = message.split()

    for word in words:
        # Extract the character code (i.e., digits at the start of the word)
        char_code = ""
        for char in word:
            if char.isdigit():
                char_code += char
            else:
                break

        # Convert the character code to the corresponding letter
        first_letter = chr(int(char_code))

        # Remove the numeric part from the word and add the first letter
        rest_of_word = word[len(char_code):]

        # If the word has more than two characters, swap the second and last character
        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]

        # Combine the first letter with the modified rest of the word
        deciphered_word = first_letter + rest_of_word
        deciphered_words.append(deciphered_word)

    # Join the deciphered words into a single string
    return " ".join(deciphered_words)

print(decipher_this(input()))
