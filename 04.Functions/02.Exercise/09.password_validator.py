def password_validator(password):
    """Check if the given password is valid."""
    errors = []

    # Check length
    if not (6 <= len(password) <= 10):
        errors.append("Password must be between 6 and 10 characters")

    # Check for valid characters
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    # Check for at least 2 digits
    digit_count = sum(c.isdigit() for c in password)
    if digit_count < 2:
        errors.append("Password must have at least 2 digits")

    # Print results
    if not errors:
        print("Password is valid")
    else:
        for error in errors:
            print(error)


# Input: Read the password from the console
password = input()

# Validate the password
password_validator(password)
