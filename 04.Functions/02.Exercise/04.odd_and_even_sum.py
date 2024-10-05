def odd_and_even_sum(number):
    # Convert the number to a string to iterate over each digit
    number_str = str(number)

    # Initialize sums for odd and even digits
    odd_sum = 0
    even_sum = 0

    # Iterate over each digit in the number
    for digit in number_str:
        digit = int(digit)  # Convert the character back to an integer

        if digit % 2 == 0:
            even_sum += digit  # Add to even sum if it's an even number
        else:
            odd_sum += digit  # Add to odd sum if it's an odd number

    # Return the result in the required format
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


# Input: Read a single number from the console
number = int(input())

# Output: Print the result
print(odd_and_even_sum(number))
