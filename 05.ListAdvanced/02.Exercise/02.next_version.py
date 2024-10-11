# Read input version
version = input()

# Split the version string into a list of integers
version_parts = list(map(int, version.split('.')))

# Increment the last part of the version
version_parts[2] += 1

# Handle overflow, if any of the parts is greater than 9
if version_parts[2] > 9:
    version_parts[2] = 0
    version_parts[1] += 1

    if version_parts[1] > 9:
        version_parts[1] = 0
        version_parts[0] += 1

# Print the next version
print(f"{version_parts[0]}.{version_parts[1]}.{version_parts[2]}")
