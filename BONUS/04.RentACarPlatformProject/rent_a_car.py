import time

# Initialize cars list
def initialize_cars():
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
    ]
    return cars

# Function to rent a car
def rent_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."

# Function to return a car
def return_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and not car["available"]:
            car["available"] = True
            return f"You have returned the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."

# Function to display all cars
def display_cars(cars):
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")

# Main menu for user interaction
def main_menu(cars):
    while True:
        print("\nWelcome to RentACar!")
        print("1. View Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        answer = input("Please choose an option (1-4): ")

        if answer == "1":
            display_cars(cars)
            input("\nPress Enter to continue...")
        elif answer == "2":
            display_cars(cars)
            car_id = int(input("Enter the car ID you want to rent: "))
            message = rent_car(cars, car_id)
            print(message)
            input("\nPress Enter to continue...")
        elif answer == "3":
            display_cars(cars)
            car_id = int(input("Enter the car ID you want to return: "))
            message = return_car(cars, car_id)
            print(message)
            input("\nPress Enter to continue...")
        elif answer == "4":
            print("Thank you for using RentACar!")
            break
        else:
            print("Invalid input. Please choose a valid option.")
            time.sleep(2)

# Run the program
if __name__ == "__main__":
    cars = initialize_cars()  # Only initialize once and pass the list around
    main_menu(cars)