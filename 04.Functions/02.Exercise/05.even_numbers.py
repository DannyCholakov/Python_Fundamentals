def even_numbers(sequence):
    # Convert the input string into a list of integers
    numbers = map(int, sequence.split())

    # Use filter() to select only even numbers
    even_nums = list(filter(lambda x: x % 2 == 0, numbers))

    return even_nums


# Input: Read a sequence of numbers as a string
sequence = input()

# Output: Print the list of even numbers
print(even_numbers(sequence))
