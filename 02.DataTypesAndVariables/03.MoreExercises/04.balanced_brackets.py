n = int(input())

is_balanced = True
opened = False

for _ in range(n):
    line = input()

    if line == '(':
        if opened:
            is_balanced = False
            break
        opened = True
    elif line == ')':
        if not opened:
            is_balanced = False
            break
        opened = False

if opened:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
