string = input().strip()
animals = [item.strip() for item in string.split(", ")]

wolf_index = animals.index('wolf')

sheep_count = len(animals) - wolf_index - 1

if wolf_index == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")



