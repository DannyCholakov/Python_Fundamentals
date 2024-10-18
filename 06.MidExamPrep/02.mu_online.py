floor_input = input().split('|')

health = 100
bitcoins = 0
room = 0

for floor in floor_input:
    room += 1
    floor_components = floor.split()
    event = floor_components[0]
    value = int(floor_components[1])

    if event == 'potion':
        healed_amount = min(100 - health, value)
        health += healed_amount
        print(f'You healed for {healed_amount} hp.')
        print(f'Current health: {health} hp.')

    elif event == 'chest':
        bitcoins += value
        print(f'You found {value} bitcoins.')

    else:
        health -= value
        if health > 0:
            print(f'You slayed {event}.')
        else:
            print(f'You died! Killed by {event}.')
            print(f'Best room: {room}')
            exit()

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
