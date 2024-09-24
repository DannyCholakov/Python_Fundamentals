start = int(input())
end = int(input())

tablepart = ''

for i in range(start, end+1):
    tablepart += chr(i) + ' '

print(tablepart)