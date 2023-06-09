# Problem 751 - Concatenation Coincidence

from decimal import Decimal


def sequence(theta: Decimal):
    k = len(str(theta)) - 2
    b = [theta]
    a = [int(theta)]
    for n in range(1, k + 1):
        b.append(int(b[n - 1]) * (b[n - 1] - int(b[n - 1]) + 1))
        a.append(int(b[n]))

    return str(a[0]) + '.' + ''.join(str(num) for num in a[1:])


def main():
    n = '2.0'
    precision = i = answer = 0  # Variable initialisation
    while precision < 26:
        for i in range(10):
            theta = Decimal(n[:-1] + str(i))
            tau = sequence(theta)
            precision = len(str(theta))
            answer = n
            # print(f'{i} -- {theta} -- {tau} -- {str(theta) <= tau} {precision}')
            if str(theta) <= tau:
                n = n[:-1] + str(i)
            else:
                n = n + str(i)
                break
        if i == 9:
            n += str(i)
    print(answer[:26])


main()
