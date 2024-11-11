def ascii_sum_between_chars(start_char, end_char, random_string):
    start_ascii = ord(start_char)
    end_ascii = ord(end_char)

    if start_ascii > end_ascii:
        start_ascii, end_ascii = end_ascii, start_ascii

    total_sum = 0
    for char in random_string:
        if start_ascii < ord(char) < end_ascii:
            total_sum += ord(char)

    return total_sum

start_char = input()
end_char = input()
random_string = input()

print(ascii_sum_between_chars(start_char, end_char, random_string))
