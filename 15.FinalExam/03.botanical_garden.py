def botanical_garden():
    plants = {}
    sections = {}

    while True:
        command = input()
        if command == "EndDay":
            break

        if command.startswith("Plant:"):
            _, data = command.split(": ")
            plant_name, water_needed, section = data.split("-")
            water_needed = int(water_needed)

            if plant_name not in plants:
                plants[plant_name] = {'water_needed': water_needed, 'section': section}
                sections[section] = sections.get(section, 0) + 1
            else:
                plants[plant_name]['water_needed'] += water_needed

        elif command.startswith("Water:"):
            _, data = command.split(": ")
            plant_name, water_amount = data.split("-")
            water_amount = int(water_amount)

            if plant_name in plants:
                plants[plant_name]['water_needed'] -= water_amount
                if plants[plant_name]['water_needed'] <= 0:
                    section = plants[plant_name]['section']
                    print(f"{plant_name} has been sufficiently watered.")
                    del plants[plant_name]

                    sections[section] -= 1
                    if sections[section] == 0:
                        del sections[section]

    if plants:
        print("Plants needing water:")
        for plant, info in plants.items():
            print(f" {plant} -> {info['water_needed']}ml left")
    else:
        print("Plants needing water:")

    if sections:
        print("Sections with thirsty plants:")
        for section, count in sections.items():
            print(f" {section}: {count}")
    else:
        print("Sections with thirsty plants:")

botanical_garden()
