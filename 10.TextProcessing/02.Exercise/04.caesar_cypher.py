def caesar_cipher(text):
    encrypted_text = ""

    for char in text:
        encrypted_text += chr(ord(char) + 3)

    return encrypted_text

input_text = input()

print(caesar_cipher(input_text))
