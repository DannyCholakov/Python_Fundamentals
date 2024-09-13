string = list(input())
list_Numbers = []
n=0

for char in string:
    if char.isupper():
        list_Numbers.append(n)
    n+=1

print(list_Numbers)


# string = input()  # No need to convert to a list, strings are iterable
# list_Numbers = [index for index, char in enumerate(string) if char.isupper()]
# print(list_Numbers)
