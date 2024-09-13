while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue

    doubled_word = ''
    for char in word:
        doubled_word += char * 2
    print(doubled_word)
