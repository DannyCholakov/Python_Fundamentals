def electron_distribution(total_electrons):
    shells = []
    n = 1  # Start with the first shell

    # Loop until we have electrons left to distribute
    while total_electrons > 0:
        # Calculate the capacity of the current shell
        shell_capacity = 2 * n ** 2

        # Place either the shell capacity or the remaining electrons, whichever is smaller
        if total_electrons >= shell_capacity:
            shells.append(shell_capacity)
            total_electrons -= shell_capacity
        else:
            shells.append(total_electrons)
            total_electrons = 0  # All electrons distributed

        # Move to the next shell
        n += 1

    return shells

num = int(input())
print(electron_distribution(num))

