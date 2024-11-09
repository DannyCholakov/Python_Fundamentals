text = input()

while text != 'end':

    text_reversed = text[::-1]
    print(f"{text} = {text_reversed}")
    text = input()
