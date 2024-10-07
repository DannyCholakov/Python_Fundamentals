command = input()
number = input()

def method(command, number):
    if command == 'int':
        number = int(number) * 2
        print(number)
    elif command == 'real':
        number = float(number) * 1.5
        print(f"{number:.2f}")
    elif command == 'string':
        print(f"${number}$")

method(command, number)
