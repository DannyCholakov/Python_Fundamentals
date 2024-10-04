# Input: Receive the string and counter n from the user
input_string = input()
n = int(input())

# Lambda function to repeat the string n times
repeat_string = lambda s, times: s * times

# Output: Print the result of the repeated string
print(repeat_string(input_string, n))
