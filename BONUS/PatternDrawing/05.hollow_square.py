square_size = int(input())

top_bottom = '*' * square_size

if square_size > 1:
    sides = '*' + ' ' * (square_size - 2) + '*'
else:
    sides = '*'  # For a square of size 1

for i in range(square_size):
    if i == 0 or i == square_size - 1:
        print(top_bottom)
    else:
        print(sides)