"""
Problem 42: Coded triangle numbers
"""

from myfunc import wordvalue

triangle = [int(n / 2 * (n + 1)) for n in range(1, 1000)]

book = open('p042_words.txt')
words = list(book)
book.close()

words = words[0].split('","')
words[0] = words[0].removeprefix('"')
words[-1] = words[-1].removesuffix('"')
words.sort()

count = 0
for i in range(len(words)):
    wordscore = wordvalue(words[i]) * (i + 1)
    if wordscore in triangle:
        count += 1

print(count)
