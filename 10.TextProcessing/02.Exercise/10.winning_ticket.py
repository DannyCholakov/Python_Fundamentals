import re

def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']

    left_half, right_half = ticket[:10], ticket[10:]

    for symbol in winning_symbols:

        escaped_symbol = re.escape(symbol)
        pattern = rf"{escaped_symbol}{{6,}}"
        left_match = re.search(pattern, left_half)
        right_match = re.search(pattern, right_half)

        if left_match and right_match:
            match_length = min(len(left_match.group()), len(right_match.group()))
            if match_length == 10:
                return f'ticket "{ticket}" - {match_length}{symbol} Jackpot!'
            else:
                return f'ticket "{ticket}" - {match_length}{symbol}'

    return f'ticket "{ticket}" - no match'

input_line = input()
tickets = [ticket.strip() for ticket in re.split(r',\s*', input_line)]

for ticket in tickets:
    print(check_ticket(ticket))
