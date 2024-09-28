factor = int(input())
n = int(input())

list_of_numbers = []
next_number = factor

for i in range(n):
    list_of_numbers.append(next_number)
    next_number += factor

print(list_of_numbers)