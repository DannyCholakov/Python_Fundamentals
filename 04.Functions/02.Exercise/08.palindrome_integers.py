def is_palindrome(num):
    """Check if a number is a palindrome."""
    num_str = str(num)  # Convert the number to a string
    return num_str == num_str[::-1]  # Check if the string is equal to its reverse


def check_palindromes(input_string):
    """Check if each number in the input string is a palindrome."""
    # Split the input string into a list of integers
    numbers = list(map(int, input_string.split(", ")))

    # Check each number and print whether it is a palindrome
    results = [is_palindrome(num) for num in numbers]

    for result in results:
        print(result)


# Input: Read a list of positive integers separated by ", "
input_string = input()

# Check for palindromes
check_palindromes(input_string)
