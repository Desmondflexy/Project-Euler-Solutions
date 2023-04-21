# Problem 79: Passcode derivation


def main():
    with open('p079_keylog.txt') as f:
        logins = set(f.read().splitlines())
        # set()^ used to remove duplicate login attempts

    x1, x2, x3 = set(), set(), set()
    for x in logins:
        x1.add(x[0])
        x2.add(x[1])
        x3.add(x[2])

    xlen = {}  # Dictionary of x with list of digits before x
    for x in x1 | x2 | x3:  # all digits in x1, x2 or x3
        xlen[x] = getDigitsBefore(x, logins)

    # Sort x in order of increasing number of digits before it
    xlen = sorted(xlen.items(), key=lambda xlen: xlen[1])
    print(''.join(item[0] for item in xlen))


def getDigitsBefore(x, logins):
    """Returns a list of digits appearing before x in logins"""
    before_x = set()
    for attempt in logins:
        if x in attempt:
            for digit in attempt:
                if digit == x:
                    break
                else:
                    before_x.add(digit)
    return before_x


main()
