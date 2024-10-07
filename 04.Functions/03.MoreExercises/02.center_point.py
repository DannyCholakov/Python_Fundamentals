import math

x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

def distance_from_origin(x, y):
    """Calculate the distance of a point from the origin (0, 0)."""
    return math.sqrt(x ** 2 + y ** 2)

def closest_point(x1, y1, x2, y2):
    """Determine which point is closer to the origin."""
    dist1 = distance_from_origin(x1, y1)
    dist2 = distance_from_origin(x2, y2)

    if dist1 < dist2:
        return (x1, y1)
    else:
        return (x2, y2)

# Output the closest point
result = closest_point(x1, y1, x2, y2)
print(result)
