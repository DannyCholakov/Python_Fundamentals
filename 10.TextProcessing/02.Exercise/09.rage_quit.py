import re

def rage_quit(input_string):
    matches = re.findall(r'(\D+)(\d+)', input_string)

    rage_message_parts = []

    for string, count in matches:
        count = int(count)
        uppercase_string = string.upper()
        rage_message_parts.append(uppercase_string * count)

    rage_message = ''.join(rage_message_parts)

    unique_symbols = set(rage_message)

    print(f"Unique symbols used: {len(unique_symbols)}")
    print(rage_message)

input_string = input()

rage_quit(input_string)
