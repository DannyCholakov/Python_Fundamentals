import math


# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Function to check which point is closer to the origin
def closer_to_origin(x1, y1, x2, y2):
    dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
    dist2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if dist1 <= dist2:
        return (math.floor(x1), math.floor(y1)), (math.floor(x2), math.floor(y2))
    else:
        return (math.floor(x2), math.floor(y2)), (math.floor(x1), math.floor(y1))


# Function to print the longer line, starting from the point closer to the origin
def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate the length of the two lines
    line1_length = calculate_distance(x1, y1, x2, y2)
    line2_length = calculate_distance(x3, y3, x4, y4)

    # If the first line is longer or equal in length to the second one
    if line1_length >= line2_length:
        point1, point2 = closer_to_origin(x1, y1, x2, y2)
        print(f"({point1[0]}, {point1[1]})({point2[0]}, {point2[1]})")
    else:
        point1, point2 = closer_to_origin(x3, y3, x4, y4)
        print(f"({point1[0]}, {point1[1]})({point2[0]}, {point2[1]})")


# Input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# Calling the function to print the result
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
