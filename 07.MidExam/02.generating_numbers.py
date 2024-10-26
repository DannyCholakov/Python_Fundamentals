list_of_numbers = list(map(int, input().split()))

while True:
    command = input()

    if command == 'END':
        break

    command_split = command.split()
    command_action = command_split[0]

    if command_action == 'add' and command_split[1] == 'to' and command_split[2] == 'start':
        numbers_to_add = list(map(int, command_split[3:]))
        list_of_numbers = numbers_to_add + list_of_numbers

    elif command_action == "remove" and command_split[1] == "greater" and command_split[2] == "than":
        threshold = int(command_split[3])
        list_of_numbers = [number for number in list_of_numbers if number <= threshold]

    elif command_action == "replace":
        value_to_replace = int(command_split[1])
        replacement = int(command_split[2])
        try:
            index = list_of_numbers.index(value_to_replace)
            list_of_numbers[index] = replacement
        except ValueError:
            pass

    elif command_action == "remove" and command_split[1] == "at":
        index = int(command_split[3])
        if 0 <= index < len(list_of_numbers):
            list_of_numbers.pop(index)

    elif command_action == "find":
        if command_split[1] == "even":
            even_numbers = [x for x in list_of_numbers if x % 2 == 0]
            print(" ".join(map(str, even_numbers)))
        elif command_split[1] == "odd":
            odd_numbers = [x for x in list_of_numbers if x % 2 != 0]
            print(" ".join(map(str, odd_numbers)))

print(", ".join(map(str, list_of_numbers)))
