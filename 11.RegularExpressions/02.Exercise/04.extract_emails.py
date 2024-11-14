import re

text = input()

regex = r'\b[a-zA-Z0-9](?!.*?[._-]{2})[a-zA-Z0-9._-]*[a-zA-Z0-9]@[a-zA-Z]+(?:-[a-zA-Z]+)*(?:\.[a-zA-Z]{2,})+\b'
matches = re.findall(regex, text)

for match in matches:
    print(match)