def string_explosion(text):
    result = []
    explosion_strength = 0

    for i in range(len(text)):
        if text[i] == '>':
            result.append(text[i])
            explosion_strength += int(text[i + 1])
        elif explosion_strength > 0:
            explosion_strength -= 1
        else:
            result.append(text[i])

    return "".join(result)

input_text = input()

print(string_explosion(input_text))
