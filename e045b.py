"""
Problem 45: Triangular, pentagonal, and hexagonal
"""

numbers = [{
    'position': 0,
    'number': 1,
    'index': 1,
    'f': lambda x: x * (x + 1) / 2
}, {
    'position': 1,
    'number': 1,
    'index': 1,
    'f': lambda x: x * (3 * x - 1) / 2
}, {
    'position': 2,
    'number': 1,
    'index': 1,
    'f': lambda x: x * (2 * x - 1)
}]

while True:
    if len(set(map(lambda x: x['number'], numbers))) == 1:
        if numbers[0]['number'] > 40755:
            print(numbers[0]['number'])
            break

    next_ = min(numbers, key=lambda x: x['number'])['position']
    numbers[next_]['index'] += 1
    numbers[next_]['number'] = numbers[next_]['f'](numbers[next_]['index'])
