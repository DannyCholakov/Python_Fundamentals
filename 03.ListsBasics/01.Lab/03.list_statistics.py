from itertools import count

numbers = int(input())

list_of_numbers = []
positives = []
negatives = []
positives_count = 0
negatives_sum = 0

for number in range(numbers):
    n = int(input())
    if n >= 0:
        positives.append(n)
        list_of_numbers.append(n)
        positives_count += 1
    elif n < 0:
        negatives.append(n)
        list_of_numbers.append(n)
        negatives_sum += n

print(positives)
print(negatives)
print(f'Count of positives: {positives_count}')
print(f'Sum of negatives: {negatives_sum}')