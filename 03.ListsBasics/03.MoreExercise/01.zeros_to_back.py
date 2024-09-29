string_of_numbers = input().split(', ')

list_of_numbers = list(map(int, string_of_numbers))

non_zero_numbers = [num for num in list_of_numbers if num != 0]

zero_count = list_of_numbers.count(0)

result = non_zero_numbers + [0] * zero_count

print(result)
