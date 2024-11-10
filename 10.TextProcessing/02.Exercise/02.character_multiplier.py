def character_multiplier(str1, str2):
    total_sum = 0
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        total_sum += ord(str1[i]) * ord(str2[i])

    if len(str1) > len(str2):
        for i in range(min_length, len(str1)):
            total_sum += ord(str1[i])
    elif len(str2) > len(str1):
        for i in range(min_length, len(str2)):
            total_sum += ord(str2[i])

    return total_sum

input_line = input()
str1, str2 = input_line.split()

print(character_multiplier(str1, str2))
