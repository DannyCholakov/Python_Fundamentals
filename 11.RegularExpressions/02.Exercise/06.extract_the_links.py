import re

text = []
while True:
    try:
        line = input()
        if line.strip() == '':
            break
        text.append(line)
    except EOFError:
        break

text = '\n'.join(text)

pattern = r'\bwww\.[A-Za-z0-9-]+(\.[a-z]{2,})+\b'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
