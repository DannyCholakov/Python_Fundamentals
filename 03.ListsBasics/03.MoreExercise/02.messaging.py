numbers = input().split()
text = list(input())

message = ""

for number in numbers:
    index = sum(int(digit) for digit in number)

    index %= len(text)
    message += text[index]
    text.pop(index)

print(message)
