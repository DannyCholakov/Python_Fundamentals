square_size = int(input())

top_bottom = ''
sides = ''
for i in range(square_size):
    top_bottom += "*"

for i in range(square_size):
    if i == 0 or i == square_size-1:
        sides += '*'
    else:
        sides += ' '

for i in range(square_size):
    if i == 0 or i == square_size-1:
        print(top_bottom)
    else:
        print(sides)
