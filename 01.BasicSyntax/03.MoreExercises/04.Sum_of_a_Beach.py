string = input().lower()
string_List = ['sun', 'sand', 'water', 'fish']

word_count = {word: 0 for word in string_List}

for word in string_List:
    count = string.count(word)
    word_count[word] += count

total_count = sum(word_count.values())
print(total_count)
