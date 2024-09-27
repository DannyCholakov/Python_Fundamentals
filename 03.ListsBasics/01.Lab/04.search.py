n = int(input())
word = input()

all_list = []
list_with_word = []

for num in range(n):
    text = input()
    if word.lower() in text.lower():
        list_with_word.append(text)
        all_list.append(text)
    else:
        all_list.append(text)

print(all_list)
print(list_with_word)