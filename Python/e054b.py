# """
# Problem 54: Poker hands
# """
# from urllib.request import urlopen
#
# card_suits = ['C', 'S', 'D', 'H']  # -> club[C], spade[S], diamond[D], heart[H]
# card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#
#
# def rank(hd):
#     """Returns the rank of a hand in the card game of poker."""
#     # Royal flush -- 10
#     for suit in card_suits:
#         cards = [val + suit for val in card_values[8:]]
#         if all([card in cards for card in hd]):
#             return 10
#     # Straight flush -- 9
#     for suit in card_suits:
#         s = [card[1] for card in hd]
#         if isconsecutive(hd) and all([k == suit for k in s]):
#             return 9
#     # Four of a kind -- 8
#     if n_of_a_kind(hd, 4) > 0:
#         return 8
#     # Full house -- 7
#     if n_of_a_kind(hd, 3) > 0 and n_of_a_kind(hd, 2) > 0:
#         return 7
#     # Flush -- 6
#     for suit in card_suits:
#         s = [card[1] for card in hd]
#         if all([k == suit for k in s]):
#             return 6
#     # Straight -- 5
#     if isconsecutive(hd):
#         return 5
#     # Three of a kind -- 4
#     if n_of_a_kind(hd, 3) > 0:
#         return 4
#     # Two pairs -- 3
#     if n_of_a_kind(hd, 2) > 1:
#         return 3
#     # One pair -- 2, otherwise High card -- 1
#     return 2 if n_of_a_kind(hd, 2) > 0 else 1
#
#
# def n_of_a_kind(hd, n):
#     """Returns number of occurrence of n of a kind."""
#     kind = {}
#     for card in hd:
#         kind.setdefault(card[0], 0)
#         kind[card[0]] += 1
#     return list(kind.values()).count(n)
#
#
# def isconsecutive(hd):
#     """Checks if card values are consecutive"""
#     f = lambda x: card_values.index(x[0])
#     i = card_values.index(min(hd, key=f)[0])
#     j = card_values.index(max(hd, key=f)[0])
#     return [k[0] for k in sorted(hd, key=f)] == card_values[i:j + 1]
#
#
# def handvalue(hd):
#     """Converts cards in hd to only values."""
#     val = [card[0] for card in hd]
#     return [card_values.index(v) + 2 for v in val]
#
#
# book = urlopen("https://projecteuler.net/project/resources/p054_poker.txt")
# player1_wins = 0
# for line in book:
#     hand = line.decode("utf-8").strip().split(' ')
#     player1 = hand[:5]
#     player2 = hand[5:]
#
#     if rank(player1) > rank(player2):
#         player1_wins += 1
#         continue
#
#     if rank(player1) == rank(player2):
#         p1 = handvalue(player1)
#         p2 = handvalue(player2)
#         # The only possibility of a draw is when: rank(player) <= 2.
#         if rank(player1) == 1:
#             a = sorted(p1, reverse=True)
#             b = sorted(p2, reverse=True)
#             if a > b:
#                 player1_wins += 1
#                 continue
#
#         if rank(player1) == 2:
#             n1 = n2 = 0
#             for n1 in p1:
#                 if p1.count(n1) == 2:
#                     break
#             for n2 in p2:
#                 if p2.count(n2) == 2:
#                     break
#             if n1 > n2:
#                 player1_wins += 1
#                 continue
#
#             if n1 == n2:
#                 for t in range(2):
#                     p1.remove(n1)
#                     p2.remove(n2)
#                 a = sorted(p1, reverse=True)
#                 b = sorted(p2, reverse=True)
#                 if a > b:
#                     player1_wins += 1
#
# print(player1_wins)
