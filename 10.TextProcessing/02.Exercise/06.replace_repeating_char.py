def replace_repeating_chars(text):
    result = []

    for i in range(len(text)):
        if i == 0 or text[i] != text[i - 1]:
            result.append(text[i])

    return "".join(result)

input_text = input()

print(replace_repeating_chars(input_text))
