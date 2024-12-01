import re

def find_hidden_eggs(text):
    pattern = r"[@#]+([a-z]{3,})[@#]+[^a-zA-Z0-9]*\/(\d+)\/"

    matches = re.findall(pattern, text)

    for color, amount in matches:
        print(f"You found {amount} {color} eggs!")

text = input()

find_hidden_eggs(text)
