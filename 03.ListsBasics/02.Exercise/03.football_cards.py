def football_game(cards_sequence):
    team_a = 11
    team_b = 11

    sent_off_a = []
    sent_off_b = []

    cards = cards_sequence.split()
    game_terminated = False

    for card in cards:
        team, player = card.split("-")
        player_number = int(player)

        if team == "A" and player_number not in sent_off_a:
            sent_off_a.append(player_number)
            team_a -= 1
            if team_a < 7:
                game_terminated = True
                break

        elif team == "B" and player_number not in sent_off_b:
            sent_off_b.append(player_number)
            team_b -= 1
            if team_b < 7:
                game_terminated = True
                break

    print(f"Team A - {team_a}; Team B - {team_b}")
    if game_terminated:
        print("Game was terminated")

football_game(input())
