def social_distribution():
    # Parse the input
    population = list(map(int, input().split(", ")))
    min_wealth = int(input())

    # Check if total wealth is sufficient
    total_wealth = sum(population)
    required_wealth = len(population) * min_wealth

    if total_wealth < required_wealth:
        print("No equal distribution possible")
        return

    # Redistribute wealth
    while any(person < min_wealth for person in population):
        # Find the index of the richest and the poorest below the minimum
        poorest_index = population.index(min(population))
        wealthiest_index = population.index(max(population))

        # Calculate how much is needed by the poorest
        needed_wealth = min_wealth - population[poorest_index]

        # Transfer wealth from the richest to the poorest
        if population[wealthiest_index] >= needed_wealth:
            population[wealthiest_index] -= needed_wealth
            population[poorest_index] += needed_wealth
        else:
            # If the wealthiest doesn't have enough to cover, transfer all
            population[poorest_index] += population[wealthiest_index]
            population[wealthiest_index] = 0

    print(population)

# Example usage:
social_distribution()
