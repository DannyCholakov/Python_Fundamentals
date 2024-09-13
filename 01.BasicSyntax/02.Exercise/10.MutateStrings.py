stringOne = input()
stringTwo = input()
newWord = ""
oldWord = ""
n = 1

for i in range(len(stringOne)):
    newWord += stringTwo[:n] + stringOne[n:]
    n += 1
    if newWord != stringOne and newWord != oldWord:
        print(newWord)
        oldWord = newWord
        newWord = ""
    else:
        newWord = ""
        continue
