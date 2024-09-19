rows = int(input("Enter the number of rows: "))

for i in range(1, rows, 2):
    spaces = ' ' * ((rows - i) // 2)
    stars = '*' * i
    print(spaces + stars)

for i in range(rows, 0, -2):
    spaces = ' ' * ((rows - i) // 2)
    stars = '*' * i
    print(spaces + stars)
