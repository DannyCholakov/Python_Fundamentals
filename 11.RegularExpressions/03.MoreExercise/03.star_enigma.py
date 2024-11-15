import re


def decrypt_message(message, key):
    return ''.join([chr(ord(char) - key) for char in message])


n = int(input())
messages = [input() for _ in range(n)]

attacked_planets = []
destroyed_planets = []

for message in messages:
    key = sum([message.lower().count(char) for char in "star"])

    decrypted_message = decrypt_message(message, key)

    planet_pattern = r'@([A-Za-z]+)[^@\-!>:]*:(\d+)[^@\-!>:]*!([AD])![^@\-!>:]*->(\d+)'
    match = re.search(planet_pattern, decrypted_message)
    if match:
        planet_name = match.group(1)
        population = int(match.group(2))
        attack_type = match.group(3)
        soldier_count = int(match.group(4))

        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
