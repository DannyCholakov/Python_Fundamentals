class Zoo:
    __animals = 0  # Class attribute to keep track of total animals

    def __init__(self, name):
        self.name = name  # The name of the zoo
        self.mammals = []  # List to store mammals
        self.fishes = []   # List to store fishes
        self.birds = []    # List to store birds

    def add_animal(self, species, name):
        """Add an animal to the respective species list and update the total count."""
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1  # Increment the total animal count

    def get_info(self, species):
        """Return formatted information based on the species and zoo name."""
        if species == 'mammal':
            species_names = ', '.join(self.mammals)
            return f"Mammals in {self.name}: {species_names}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            species_names = ', '.join(self.fishes)
            return f"Fishes in {self.name}: {species_names}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            species_names = ', '.join(self.birds)
            return f"Birds in {self.name}: {species_names}\nTotal animals: {Zoo.__animals}"
        else:
            return f"No information available for species: {species}"


# Input handling
zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())  # Number of animals to be added

# Process each animal input and add them to the zoo
for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

# Get the species to fetch info
species_to_check = input()

# Output the information for the specified species
print(zoo.get_info(species_to_check))
