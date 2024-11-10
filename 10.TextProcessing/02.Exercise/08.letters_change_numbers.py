def get_alphabet_position(letter):
    return ord(letter.lower()) - ord('a') + 1

def process_string(string):
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    if first_letter.isupper():
        result = number / get_alphabet_position(first_letter)
    else:
        result = number * get_alphabet_position(first_letter)

    if last_letter.isupper():
        result -= get_alphabet_position(last_letter)
    else:
        result += get_alphabet_position(last_letter)

    return result

input_text = input()
strings = input_text.split()

total_sum = sum(process_string(string) for string in strings)

print(f"{total_sum:.2f}")
