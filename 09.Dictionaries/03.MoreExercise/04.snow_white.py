dwarfs = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)

    key = (dwarf_name, hat_color)

    if key not in dwarfs or dwarfs[key] < physics:
        dwarfs[key] = physics

hat_color_count = {}
for (name, color), physics in dwarfs.items():
    if color not in hat_color_count:
        hat_color_count[color] = 0
    hat_color_count[color] += 1

sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda item: (-item[1], -hat_color_count[item[0][1]])
)

for (name, color), physics in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")
