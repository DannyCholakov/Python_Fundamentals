def anonymous_threat(data):
    while True:
        command = input().split()

        # Stop when "3:1" command is encountered
        if command[0] == "3:1":
            break

        if command[0] == "merge":
            start_index = max(0, int(command[1]))  # Ensure start is within bounds
            end_index = min(len(data) - 1, int(command[2]))  # Ensure end is within bounds

            # Merge the elements from start_index to end_index
            merged_part = ''.join(data[start_index:end_index + 1])

            # Replace the merged elements with the new merged string
            data = data[:start_index] + [merged_part] + data[end_index + 1:]

        elif command[0] == "divide":
            index = int(command[1])
            partitions = int(command[2])

            element = data[index]
            part_size = len(element) // partitions
            remainder = len(element) % partitions

            # Split the element into partitions
            divided_parts = []
            start = 0
            for i in range(partitions):
                if i == partitions - 1:  # Last partition gets the remainder
                    divided_parts.append(element[start:])
                else:
                    divided_parts.append(element[start:start + part_size])
                    start += part_size

            # Replace the element at index with the divided parts
            data = data[:index] + divided_parts + data[index + 1:]

    # Print the final state of the data list
    print(' '.join(data))


# Example usage:
data_input = input().split()  # Input the initial data
anonymous_threat(data_input)
