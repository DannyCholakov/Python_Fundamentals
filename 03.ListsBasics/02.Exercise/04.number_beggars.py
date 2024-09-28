def beggars_collect(numbers_str, beggar_count):
    numbers = [int(x) for x in numbers_str.split(", ")]

    sums = [0] * beggar_count

    for i, num in enumerate(numbers):
        beggar_index = i % beggar_count
        sums[beggar_index] += num
    return sums

numbers_input = input()
beggar_count = int(input())

result = beggars_collect(numbers_input, beggar_count)
print(result)
