def sort_numbers(sequence):
    # Convert the input string into a list of integers
    numbers = list(map(int, sequence.split()))

    # Use sorted() to sort the numbers in ascending order
    sorted_nums = sorted(numbers)

    return sorted_nums


# Input: Read a sequence of numbers as a string
sequence = input()

# Output: Print the sorted list of numbers
print(sort_numbers(sequence))
