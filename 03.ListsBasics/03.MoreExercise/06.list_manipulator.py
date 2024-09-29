def process_commands(num_list):
    while True:
        command = input()
        if command == "end":
            break
        command_parts = command.split()
        action = command_parts[0]

        if action == "exchange":
            index = int(command_parts[1])
            if 0 <= index < len(num_list):
                num_list = num_list[index + 1:] + num_list[:index + 1]
            else:
                print("Invalid index")

        elif action == "max":
            even_odd = command_parts[1]
            filtered_nums = [num for num in num_list if
                             (num % 2 == 0 and even_odd == "even") or (num % 2 != 0 and even_odd == "odd")]
            if filtered_nums:
                max_num = max(filtered_nums)
                max_index = len(num_list) - 1 - num_list[::-1].index(max_num)
                print(max_index)
            else:
                print("No matches")

        elif action == "min":
            even_odd = command_parts[1]
            filtered_nums = [num for num in num_list if
                             (num % 2 == 0 and even_odd == "even") or (num % 2 != 0 and even_odd == "odd")]
            if filtered_nums:
                min_num = min(filtered_nums)
                min_index = len(num_list) - 1 - num_list[::-1].index(min_num)
                print(min_index)
            else:
                print("No matches")

        elif action == "first":
            count = int(command_parts[1])
            even_odd = command_parts[2]
            if count > len(num_list):
                print("Invalid count")
            else:
                filtered_nums = [num for num in num_list if
                                 (num % 2 == 0 and even_odd == "even") or (num % 2 != 0 and even_odd == "odd")]
                print(filtered_nums[:count])

        elif action == "last":
            count = int(command_parts[1])
            even_odd = command_parts[2]
            if count > len(num_list):
                print("Invalid count")
            else:
                filtered_nums = [num for num in num_list if
                                 (num % 2 == 0 and even_odd == "even") or (num % 2 != 0 and even_odd == "odd")]
                print(filtered_nums[-count:])

    print(f"[{', '.join(map(str, num_list))}]")

initial_list = list(map(int, input().split()))
process_commands(initial_list)
