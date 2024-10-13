def take_skip_rope(input_string):
    numbers = []
    non_numbers = []

    # Separate digits and non-digits
    for char in input_string:
        if char.isdigit():
            numbers.append(int(char))
        else:
            non_numbers.append(char)

    # Split numbers into take and skip lists
    take_list = numbers[::2]  # Even-indexed numbers
    skip_list = numbers[1::2]  # Odd-indexed numbers

    result = []
    current_index = 0

    # Iterate over both take and skip lists
    for take, skip in zip(take_list, skip_list):
        # Take `take` characters
        result.append(''.join(non_numbers[current_index:current_index + take]))
        # Skip `skip` characters
        current_index += take + skip

    # Join and print the result
    print(''.join(result))

# Example usage:
input_string = input()  # Read input
take_skip_rope(input_string)
