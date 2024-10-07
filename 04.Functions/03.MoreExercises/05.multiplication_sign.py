def multiplication_sign(a, b, c):
    # Check if any number is zero
    if a == 0 or b == 0 or c == 0:
        print("zero")
        return

    # Count the negative numbers
    negatives = 0
    if a < 0:
        negatives += 1
    if b < 0:
        negatives += 1
    if c < 0:
        negatives += 1

    # If there's an odd number of negative values, the result is negative
    if negatives % 2 != 0:
        print("negative")
    else:
        print("positive")


# Input
a = int(input())
b = int(input())
c = int(input())

# Call the function to determine the sign of the multiplication
multiplication_sign(a, b, c)
