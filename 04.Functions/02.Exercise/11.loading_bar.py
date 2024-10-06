def loading_bar(percentage):
    """Return a loading bar based on the given percentage."""
    if percentage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        # Calculate the number of filled and empty segments in the loading bar
        filled_length = percentage // 10
        empty_length = 10 - filled_length

        # Create the loading bar string
        loading_bar = f"{percentage}% [{'%' * filled_length}{'.' * empty_length}]"
        return f"{loading_bar}\nStill loading..."


# Input: Read the percentage from the console
number = int(input())

# Check if the input number is valid
if number % 10 == 0 and 0 <= number <= 100:
    result = loading_bar(number)
    print(result)
else:
    print("Input must be an integer between 0 and 100, inclusive, and divisible by 10.")
