numbers_string = input()
numbers_list = list(map(int, numbers_string.split()))

n = int(input())
sorted_list = sorted(numbers_list)

numbers_to_remove = sorted_list[:n]

remaining_numbers = [num for num in numbers_list if num not in numbers_to_remove]

print(", ".join(map(str, remaining_numbers)))
