import re

# Input string
numbers_string = input()

# Regular expression to match numbers without leading zeros before the decimal
regex = r'(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))'

# Find all matches using re.findall
matches = re.finditer(regex, numbers_string)

# Extract and print matches separated by spaces
result = [match.group() for match in matches]
print(" ".join(result))
