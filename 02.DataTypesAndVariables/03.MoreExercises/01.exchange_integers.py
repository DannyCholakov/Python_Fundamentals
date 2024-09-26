a = int(input())
b = int(input())

c = a
a = b
b = c

print('Before:')
print(f'a = {c}')
print(f'b = {a}')
print('After:')
print(f'a = {a}')
print(f'b = {b}')