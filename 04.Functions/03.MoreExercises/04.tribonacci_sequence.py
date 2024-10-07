def tribonacci_sequence(n):
    # If n is 1, just print the first number
    if n == 1:
        print(1)
        return
    # Initialize the first three elements of the Tribonacci sequence
    sequence = [1, 1, 2]

    # If n is less than or equal to 3, slice the list accordingly
    if n <= 3:
        print(' '.join(map(str, sequence[:n])))
        return

    # Generate the rest of the sequence until it reaches the length n
    for i in range(3, n):
        next_value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_value)

    # Print the sequence with numbers separated by a single space
    print(' '.join(map(str, sequence)))


# Input
n = int(input())

# Call the function to print the Tribonacci sequence
tribonacci_sequence(n)
