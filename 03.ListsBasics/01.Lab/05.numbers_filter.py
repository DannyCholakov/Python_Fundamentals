n = int(input())

list_numbers = []
new_list = []

for i in range(n):
    new_number = int(input())
    list_numbers.append(new_number)

command = input()

for number in list_numbers:
    if command == 'even' and number % 2 == 0:
        new_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        new_list.append(number)
    elif command == 'positive' and number >= 0:
        new_list.append(number)
    elif command == 'negative' and number < 0:
        new_list.append(number)

print(new_list)