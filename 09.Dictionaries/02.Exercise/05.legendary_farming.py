# Initialize materials and legendary items
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

# Flag to check if a legendary item is obtained
obtained = False

while not obtained:
    line = input().split()

    # Process each material and quantity in the input line
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                print(f"{legendary_items[material]} obtained!")
                obtained = True
                break
        else:
            if material in junk_materials:
                junk_materials[material] += quantity
            else:
                junk_materials[material] = quantity

# Output the key materials
for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

# Output the junk materials
for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")
