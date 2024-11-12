import random

# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
    # Declare a string variable
    string_var = input("Declare a string: ")

    # Split the string into words
    words = string_var.split()

    # Extract and print a random word from the sentence
    if words:
        random_word = words[random.randint(0, len(words) - 1)]
        print(f"Extracted word: {random_word}")

    # Convert the entire sentence to uppercase and print it
    string_var_upper = string_var.upper()
    print(f"Uppercase sentence: {string_var_upper}")

    # Replace a word in the sentence and print the modified sentence
    if words:
        # Replacing a random word with "awesome"
        index_to_replace = random.randint(0, len(words) - 1)
        words[index_to_replace] = "awesome"
        modified_sentence = " ".join(words)
        print(f"Modified sentence: {modified_sentence}")

# If the user chooses Numbers (choice == '2'):
elif choice == '2':
# Prompt the user to input two numbers, e.g., num1 and num2.
    print('Input 2 numbers:')
    number_one = float(input("Declare the first number: "))
    number_two = float(input("Declare the second number: "))
# Perform and print the results of addition, subtraction, multiplication, and division.
    print(f"Addition: {number_one + number_two}")
    print(f"Subtraction: {number_one - number_two}")
    print(f"Multiplication: {number_one * number_two}")

# Handle division by zero (e.g., print an error message if num2 is zero).
    if number_two == 0:
        print('Cannot divide by zero!')
    else:
        print(f"Division: {number_one / number_two}")

# Perform a power operation, raising num1 to the power of num2, and print the result.
    print(f'Raising {number_one} to the power of {number_two}: {number_one ** number_two}')

# If the user chooses Booleans (choice == '3'):
elif choice == '3':
    # Declare two boolean variables
    is_python_fun = True
    is_sunny = False

    # Perform and print the results of logical operations: AND, OR, NOT
    print(f"Logical Operations:")
    print(f"is_python_fun AND is_sunny: {is_python_fun and is_sunny}")
    print(f"is_python_fun OR is_sunny: {is_python_fun or is_sunny}")
    print(f"NOT is_python_fun: {not is_python_fun}")
    print(f"NOT is_sunny: {not is_sunny}")

    # Perform and print the results of comparison operations
    print(f"\nComparison Operations:")
    print(f"10 > 5: {10 > 5}")
    print(f"5 == 5: {5 == 5}")
    print(f"7 < 3: {7 < 3}")
    print(f"10 >= 10: {10 >= 10}")
    print(f"4 != 2: {4 != 2}")

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans)
    mixed_list = [42, "Hello", True, 3.14, "Python"]
    print(f"Mixed List: {mixed_list}")
    # Append a new element to the list and print the updated list
    mixed_list.append("New Element")
    print("Updated List:", mixed_list)

    # Access and print the 4th element in the list (index 3)
    if len(mixed_list) > 3:
        print("4th element in the list:", mixed_list[3])
    else:
        print("The list does not have enough elements.")

    ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits)
    fruits = ("apple", "banana", "cherry", "date")

    # Print the length of the tuple
    print("\nLength of the tuple:", len(fruits))

    # Try to modify one element in the tuple and handle the resulting TypeError
    try:
        fruits[1] = "blueberry"
    except TypeError as e:
        print("Error: Cannot modify an element in a tuple. Tuples are immutable.")
        print("Exception message:", e)

    ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city)
    person_info = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland"
    }

    # Access and print the value for one of the keys (e.g., "age")
    print("\nValue for 'age' key:", person_info["age"])

    # Add a new key-value pair to the dictionary and print the updated dictionary
    person_info["profession"] = "Explorer"
    print("Updated Dictionary:", person_info)

# If the user enters an invalid choice:
else:
# Print an error message indicating an invalid selection.
    print('Invalid input!')

