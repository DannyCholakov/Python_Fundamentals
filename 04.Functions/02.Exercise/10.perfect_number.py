def is_perfect_number(num):
    """Check if the given number is a perfect number."""
    if num < 1:
        return "It's not so perfect."  # Perfect numbers must be positive integers

    # Calculate the sum of proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)

    # Check if the sum of divisors equals the original number
    if divisor_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


# Input: Read the number from the console
number = int(input())

# Check if the number is perfect and print the result
result = is_perfect_number(number)
print(result)
