def water_overflow():
    capacity = 255
    current_water = 0

    n = int(input())

    for _ in range(n):
        liters = int(input())
        if current_water + liters > capacity:
            print("Insufficient capacity!")
        else:
            current_water += liters

    print(current_water)

water_overflow()
