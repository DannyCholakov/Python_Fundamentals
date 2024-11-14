import re

text = input()

regex = r'\b[a-zA-Z0-9]+[\w.-]*@[a-zA-Z]+(?:-[a-zA-Z]+)*(?:\.[a-zA-Z]+)+\b'
matches = re.findall(regex, text)

for match in matches:
    print(match)


