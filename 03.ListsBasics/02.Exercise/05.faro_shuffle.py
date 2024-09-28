def faro_shuffle(deck, shuffle_count):
    for _ in range(shuffle_count):
        half = len(deck) // 2
        first_half = deck[:half]
        second_half = deck[half:]

        shuffled_deck = []
        for i in range(half):
            shuffled_deck.append(first_half[i])
            shuffled_deck.append(second_half[i])

        deck = shuffled_deck

    return deck

deck_input = input().split()
shuffle_count = int(input())

shuffled_deck = faro_shuffle(deck_input, shuffle_count)
print(shuffled_deck)
