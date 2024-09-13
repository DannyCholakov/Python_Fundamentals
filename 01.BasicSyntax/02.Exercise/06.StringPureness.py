n = int(input())

for i in range(n):
    string = input()
    for word in range(len(string)):
        slice = string[word]
        if slice ==',' or slice =='.' or slice=='_':
            print(f'{string} is not pure!')
            break
        else:
            continue
    else:
        print(f'{string} is pure.')
