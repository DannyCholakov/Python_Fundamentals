size = int(input("Enter the size: "))

for i in range(size):
    row = ""
    for j in range(size):
        if (i + j) % 2 == 0:
            row += "*"
        else:
            row += "-"
    print(row)
