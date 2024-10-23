class Circle:
    __pi = 3.14  # Class attribute for pi

    def __init__(self, diameter):
        self.radius = diameter / 2  # Calculate the radius from the diameter

    def calculate_circumference(self):
        """Returns the circumference of the circle."""
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        """Returns the area of the circle."""
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):
        """Returns the area of the sector based on the given angle."""
        return (angle / 360) * self.calculate_area()


# Test the class
circle = Circle(10)  # Circle with a diameter of 10
angle = 5            # Sector angle

# Print results formatted to 2 decimal places
print(f"{circle.calculate_circumference():.2f}")  # Expected output: 31.40
print(f"{circle.calculate_area():.2f}")           # Expected output: 78.50
print(f"{circle.calculate_area_of_sector(angle):.2f}")  # Expected output: 1.09
