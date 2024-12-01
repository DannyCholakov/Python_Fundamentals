word = input()

while True:
    command = input()
    if command == "Abracadabra":
        break

    spell = command.split()

    if spell[0] == "Abjuration":
        word = word.upper()
        print(word)

    elif spell[0] == "Necromancy":
        word = word.lower()
        print(word)

    elif spell[0] == "Illusion":
        try:
            index = int(spell[1])
            letter = spell[2]
            if 0 <= index < len(word):
                word = word[:index] + letter + word[index + 1:]
                print("Done!")
            else:
                print("The spell was too weak.")
        except (ValueError, IndexError):
            print("The spell was too weak.")

    elif spell[0] == "Divination":
        first_substring = spell[1]
        second_substring = spell[2]
        if first_substring in word:
            word = word.replace(first_substring, second_substring)
            print(word)
        else:
            continue

    elif spell[0] == "Alteration":
        substring = spell[1]
        if substring in word:
            word = word.replace(substring, "")
            print(word)
        else:
            continue

    else:
        print("The spell did not work!")
