DEFAULT_DAMAGE = 45
DEFAULT_HEALTH = 250
DEFAULT_ARMOR = 10

dragons = {}

n = int(input())
for _ in range(n):
    dragon_input = input().split()
    dragon_type = dragon_input[0]
    dragon_name = dragon_input[1]
    damage = dragon_input[2]
    health = dragon_input[3]
    armor = dragon_input[4]


    damage = int(damage) if damage != "null" else DEFAULT_DAMAGE
    health = int(health) if health != "null" else DEFAULT_HEALTH
    armor = int(armor) if armor != "null" else DEFAULT_ARMOR

    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][dragon_name] = {"damage": damage, "health": health, "armor": armor}

for dragon_type, dragon_data in dragons.items():

    total_damage = sum(d["damage"] for d in dragon_data.values())
    total_health = sum(d["health"] for d in dragon_data.values())
    total_armor = sum(d["armor"] for d in dragon_data.values())
    count = len(dragon_data)

    avg_damage = total_damage / count
    avg_health = total_health / count
    avg_armor = total_armor / count

    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for dragon_name in sorted(dragon_data.keys()):
        stats = dragon_data[dragon_name]
        print(f"-{dragon_name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
