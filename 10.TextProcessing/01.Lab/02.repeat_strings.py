text = input().split()

string_new = ''

for word in text:
    length = len(word)
    string_new += word * length

print(string_new)