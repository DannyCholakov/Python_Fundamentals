import re

def calculate_health(demon_name):
    health_pattern = r'[^0-9+\-*\/.]'
    health_chars = re.findall(health_pattern, demon_name)
    return sum(ord(char) for char in health_chars)

def calculate_damage(demon_name):
    damage_pattern = r'[+-]?\d+\.?\d*'
    damage_values = re.findall(damage_pattern, demon_name)
    base_damage = sum(float(value) for value in damage_values)

    for char in demon_name:
        if char == '*':
            base_damage *= 2
        elif char == '/':
            base_damage /= 2

    return base_damage

demon_names = input().split(',')

demon_names = [demon.strip() for demon in demon_names]

demons = {}

for demon in demon_names:
    health = calculate_health(demon)
    damage = calculate_damage(demon)
    demons[demon] = (health, damage)

sorted_demons = sorted(demons.items())

for demon, (health, damage) in sorted_demons:
    print(f"{demon} - {health} health, {damage:.2f} damage")
