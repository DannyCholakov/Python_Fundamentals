def morse_to_english(morse_code):
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z"
    }

    words = morse_code.split(" | ")

    translated_words = []

    for word in words:
        letters = word.split()
        translated_word = ''.join(morse_dict[letter] for letter in letters)
        translated_words.append(translated_word)

    return ' '.join(translated_words)

morse_code = input()

print(morse_to_english(morse_code))
