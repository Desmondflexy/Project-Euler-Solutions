"""
Problem 54: Poker hands
"""
# -> club[C], spade[S], diamond[D], heart[H]
card_suits = ['C', 'S', 'D', 'H']
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def rank(hd: list[str]):
    """Returns the rank of a hand in the card game of poker."""

    def n_of_a_kind(n):
        """Returns number of occurrence of n of a kind."""
        kind = {}
        for card in hd:
            kind.setdefault(card[0], 0)
            kind[card[0]] += 1
        return list(kind.values()).count(n)

    def isconsecutive():
        """Checks if card values are consecutive"""

        def f(x): return card_values.index(x[0])

        i = card_values.index(min(hd, key=f)[0])
        j = card_values.index(max(hd, key=f)[0])
        return [k[0] for k in sorted(hd, key=f)] == card_values[i:j + 1]

    # Royal flush -- 10
    for suit in card_suits:
        cards = [val + suit for val in card_values[8:]]
        if all([card in cards for card in hd]):
            return 10

    # Straight flush -- 9
    for suit in card_suits:
        s = [card[1] for card in hd]
        if isconsecutive() and all([k == suit for k in s]):
            return 9

    # Four of a kind -- 8
    if n_of_a_kind(4) > 0:
        return 8

    # Full house -- 7
    if n_of_a_kind(3) > 0 and n_of_a_kind(2) > 0:
        return 7

    # Flush -- 6
    for suit in card_suits:
        s = [card[1] for card in hd]
        if all([k == suit for k in s]):
            return 6

    # Straight -- 5
    if isconsecutive():
        return 5

    # Three of a kind -- 4
    if n_of_a_kind(3) > 0:
        return 4

    # Two pairs -- 3
    if n_of_a_kind(2) > 1:
        return 3

    # One pair -- 2, otherwise High card -- 1
    return 2 if n_of_a_kind(2) > 0 else 1


def handvalue(hd):
    """Converts cards in hd to values in descending order."""
    val = [card[0] for card in hd]
    lst = [card_values.index(v) + 2 for v in val]
    return sorted(lst, reverse=True)


book = open('p054_poker.txt')
player1_wins = 0
results = 0
sn = 1
for line in book:
    hand = line.strip().split(' ')
    player1 = hand[:5]
    player2 = hand[5:]
    r1 = rank(player1)
    r2 = rank(player2)

    if r1 > r2:
        player1_wins += 1
        winner = 'player1 wins (rank)'
    elif r1 < r2:
        winner = 'player2 wins (rank)'
    else:
        p1 = handvalue(player1)
        p2 = handvalue(player2)
        # The only possibility of a draw is when: rank(player) <= 2.
        if r1 == 1:
            # High Card: Highest value card
            if p1 > p2:
                player1_wins += 1
                winner = 'player1 wins (highest card)'
            elif p1 < p2:
                winner = 'player2 wins (highest card)'
            else:  # Very rare for both players to have the same values
                winner = 'draw'
        else:  # r1 = r2 = 2
            # One Pair: Two cards of the same value
            a = [p1.count(i) for i in p1]
            n1 = p1[a.index(2)]
            b = [p2.count(i) for i in p2]
            n2 = p2[b.index(2)]

            if n1 > n2:
                player1_wins += 1
                winner = 'player1 wins (one pair)'
            elif n1 < n2:
                winner = 'player2 wins (one pair)'
            else:
                for _ in range(2):
                    p1.remove(n1)
                    p2.remove(n2)
                if p1 > p2:
                    player1_wins += 1
                    winner = 'player1 wins (one pair, highest cards)'
                elif p1 < p2:
                    winner = 'player2 wins (one pair, highest cards)'
                else:  # very rare
                    winner = 'draw'

    x = 1
    if (r1 >= x or r2 >= x) and 'player1' in winner:
        results += 1
        print(f"{sn:4d} {player1} {r1} -- {r2} {player2} -- {winner}")
    sn += 1
print(results)
book.close()
