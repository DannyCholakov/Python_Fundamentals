rows = int(input("Enter the number of rows: "))

for i in range(rows, 0,-1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
