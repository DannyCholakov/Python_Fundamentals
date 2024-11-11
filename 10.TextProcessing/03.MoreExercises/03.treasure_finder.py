def decrypt_message(message, key):
    decrypted_message = []
    key_length = len(key)

    for index, char in enumerate(message):
        key_value = key[index % key_length]
        decrypted_char = chr(ord(char) - key_value)
        decrypted_message.append(decrypted_char)

    return ''.join(decrypted_message)

def find_treasure(message):
    treasure_type_start = message.find('&') + 1
    treasure_type_end = message.find('&', treasure_type_start)
    treasure_type = message[treasure_type_start:treasure_type_end]

    coordinates_start = message.find('<') + 1
    coordinates_end = message.find('>', coordinates_start)
    coordinates = message[coordinates_start:coordinates_end]

    return treasure_type, coordinates

key = list(map(int, input().split()))

while True:
    line = input()
    if line == "find":
        break

    decrypted_message = decrypt_message(line, key)

    treasure_type, coordinates = find_treasure(decrypted_message)
    print(f"Found {treasure_type} at {coordinates}")
