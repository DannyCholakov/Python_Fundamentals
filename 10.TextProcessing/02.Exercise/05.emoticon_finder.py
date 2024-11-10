def find_emoticons(text):
    emoticons = []

    for i in range(len(text) - 1):
        if text[i] == ":" and not text[i + 1].isspace():
            emoticons.append(text[i:i + 2])

    return emoticons

input_text = input()

emoticons = find_emoticons(input_text)
for emoticon in emoticons:
    print(emoticon)
