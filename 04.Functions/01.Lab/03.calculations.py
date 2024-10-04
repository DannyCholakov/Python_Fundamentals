def calculations(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 // num2  # Use integer division (//) as the inputs are integers
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2

# Input: Receive the operator and two numbers from the user
operator = input()
num1 = int(input())
num2 = int(input())

# Output: Print the result of the operation
print(calculations(operator, num1, num2))
