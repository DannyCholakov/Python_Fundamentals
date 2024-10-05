def sum_numbers(a, b):
    return a + b

def subtract(sum_result, c):
    return sum_result - c

def add_and_subtract(a, b, c):
    sum_result = sum_numbers(a, b)
    return subtract(sum_result, c)

# Input: reading three integers from the console
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Output: print the result of add_and_subtract function
print(add_and_subtract(num1, num2, num3))
