coffees = 0
while True:
    command = input()

    if command == 'END':
        if coffees > 5:
            print('You need extra sleep')
        else:
            print(coffees)
        break
    elif command =='coding' or command =='dog' or command =='cat' or command =='movie':
        coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        coffees += 2
    else:
        continue


# coffees = 0
# while True:
#     command = input()
#
#     if command == 'END':
#         if coffees > 5:
#             print('You need extra sleep')
#         else:
#             print(coffees)
#         break
#
#
#     events = ['coding', 'dog', 'cat', 'movie']
#
#     if command.lower() in events:
#         if command.islower():
#             coffees += 1
#         else:
#             coffees += 2
