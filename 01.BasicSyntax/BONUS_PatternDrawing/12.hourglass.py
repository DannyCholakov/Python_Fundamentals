rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    spaces = ' ' * (rows - i)
    pattern = '* ' * i
    print(spaces + pattern.strip())

for i in range(2, rows + 1):
    spaces = ' ' * (rows - i)
    pattern = '* ' * i
    print(spaces + pattern.strip())
