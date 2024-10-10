# Step 1: Read input
happiness_values = list(map(int, input().split()))  # Parse the happiness values as a list of integers
factor = int(input())  # Parse the happiness improvement factor as an integer

# Step 2: Multiply each happiness value by the factor
improved_happiness = list(map(lambda x: x * factor, happiness_values))

# Step 3: Calculate the average happiness
average_happiness = sum(improved_happiness) / len(improved_happiness)

# Step 4: Count how many employees have happiness greater than or equal to the average
happy_count = len([h for h in improved_happiness if h >= average_happiness])

# Step 5: Print the result based on the happy count
total_count = len(improved_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
