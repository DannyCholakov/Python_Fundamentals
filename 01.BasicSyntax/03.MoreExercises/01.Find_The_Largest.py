number = list(input())

newNumber = sorted(number, reverse=True)
newNumber = ''.join(newNumber)

print(int(newNumber))
