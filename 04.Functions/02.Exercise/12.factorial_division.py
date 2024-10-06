import math

def factorial_division(num1, num2):
    # Calculate the factorial of both numbers
    factorial_num1 = math.factorial(num1)
    factorial_num2 = math.factorial(num2)

    # Divide the first factorial by the second
    result = factorial_num1 / factorial_num2

    # Print the result formatted to two decimal places
    print(f"{result:.2f}")


# Input
number1 = int(input())
number2 = int(input())

# Call the function
factorial_division(number1, number2)
