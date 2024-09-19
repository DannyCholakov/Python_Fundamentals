rows = int(input())

for i in range(1, rows + 1):

    spaces = ' ' * (rows - i)
    ascending = ''.join(str(j) for j in range(1, i + 1))
    descending = ''.join(str(j) for j in range(i - 1, 0, -1))

    print(spaces + ascending + descending)

for i in range(rows - 1, 0, -1):

    spaces = ' ' * (rows - i)
    ascending = ''.join(str(j) for j in range(1, i + 1))
    descending = ''.join(str(j) for j in range(i - 1, 0, -1))

    print(spaces + ascending + descending)
