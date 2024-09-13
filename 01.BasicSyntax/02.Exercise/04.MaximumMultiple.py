divisor = int(input())
boundary = int(input())

largestInteger = 0

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        largestInteger = i
        break

print(largestInteger)