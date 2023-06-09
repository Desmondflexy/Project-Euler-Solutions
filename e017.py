"""
Problem 17 - Number letter counts
"""
# 1 -- 20, 30, 40, ..., 90
num2word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
            8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
            13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eigtheen', 19: 'nineteen', 20: 'twenty',
            30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
            80: 'eigthy', 90: 'ninety'
            }
# 21 -- 99
for T in range(20, 100, 10):
    for U in range(1, 10):
        num2word[T + U] = num2word[T] + num2word[U]

# 100 -- 999
for H in range(100, 1000, 100):
    num2word[H] = num2word[H / 100] + 'hundred'
    for TU in range(1, 100):
        num2word[H + TU] = num2word[H] + 'and' + num2word[TU]

# 1000
num2word[1000] = 'onethousand'

print(sum([len(i) for i in list(num2word.values())]))
