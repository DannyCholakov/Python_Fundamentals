import re

text = ''
while True:
    try:
        line = input()
        if line == '':
            break
        text += line + '\n'
    except EOFError:
        break

pattern = r'www\.[A-Za-z0-9\-]+(\.[a-z0-9]+)+'
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
