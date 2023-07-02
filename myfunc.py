"""Helper functions"""
# ================================================================

from math import sqrt, gcd


def divisors(n):
    """Lists the divisors of a number"""
    if n < 1:
        raise Exception('encountered a non-positive input')
    A, B = [], []
    a = b = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n // i
            A.append(a)
            B.append(b)
    if a == b:
        B.pop()
    B.reverse()
    return A + B


def lcm(a, b):
    '''Calculates the LCM of two numbers.'''
    return a * (b // gcd(a, b))


# def fibs(n):
#     '''Generates the first n members of fibonacci sequence.'''
#     f = [1, 1]
#     [f.append(f[i - 2] + f[i - 1]) for i in range(2, n)]
#     return f


def fibs(n):
    '''Generates the first n members of fibonacci sequence.'''
    temp1, temp2 = 0, 1
    i = 0
    while i < n:
        yield temp1
        temp3 = temp1 + temp2
        temp1 = temp2
        temp2 = temp3
        i += 1


def array2num(lst):
    '''Converts array to digits'''
    return int(''.join(str(num) for num in lst))


def num2array(num):
    """Converts digits to array"""
    return [int(i) for i in str(num)]


def isprime(n):
    'Primality testing'
    if n < 0:
        raise Exception('Argument must not be a negative number')
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    f = 5
    while f <= int(sqrt(n)):
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def primes(n):
    'Lists all primes upto n'
    n = int(n)
    p = list(range(1, n + 1, 2))
    q = len(p)
    p[0] = 2
    for k in range(3, int(sqrt(n)) + 1, 2):
        if p[(k + 1) // 2 - 1]:
            for i in range((k * k + 1) // 2 - 1, q, k):
                p[i] = 0
                del i
    return [i for i in p if i > 0]


def ndivs(n):
    'Counts divisors of a number'
    k = 0
    z = int(sqrt(n))
    for i in range(1, z + 1):
        if n % i == 0:
            k += 2
    if z * z == n:
        k -= 1
    return k


def factor(n):
    'Returns the prime factors of a number'
    i = 2
    f = []
    while i * i <= n:
        if n % i == 0:
            f.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        f.append(n)
    return f


def nthfib(n):
    'Returns the nth term in the fibonacci series'
    f = 0, 1
    for i in range(1, n - 1):
        f = f[1], sum(f)
    return sum(f)


def ispandigital(num, a=1, b=9):
    'Checks if a number is a through b pandigital'
    li = num2array(num)
    r = range(a, b + 1)
    length = len(r)
    if len(li) != length:
        return False
    li.sort()
    i = 0
    while i < length and li[i] == r[i]:
        i += 1
    if i != length:
        return False
    return True


def phi(n):
    '''Counts positive integers less than n that are relatively prime to n'''
    if isprime(n):
        return n - 1
    p = set(factor(n))
    y = n
    for i in p:
        y *= (1 - 1 / i)
    return int(y)


def ispalindrome(n):
    'Checks if a number is palindrome'
    return str(n) == str(n)[::-1]


def base(num, x=10, y=2):
    '''Converts a number in base x to a number in base y'''
    if x > 10 or y > 10:
        return print('!!! error: base > 10')
    if x == y:
        return num
    # Convert from base x to base 10
    m, p = 0, 0
    while num > 0:
        a = num % 10
        if a >= x:
            return print('!!! error: digit >= base')
        m += a * x ** p
        num //= 10
        p += 1
    if y == 10:
        return m

    # Convert from base 10 to base y
    num = m
    m, p = 0, 0
    while num > 0:
        m += (num % y) * 10 ** p
        num //= y
        p += 1
    return m


alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
         'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def wordvalue(word):
    '''Returns the numerical value of a word (string).
       Project Euler problem 22.'''
    word = word.upper()
    w = list(word)
    value = sum([alpha[w[i]] for i in range(len(w))])
    return value


def reverse(num):
    '''Reverses the digits of a number.'''
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev


def nextprime(n):
    while True:
        n += 1
        if isprime(n):
            return n


def prevprime(n):
    while True:
        n -= 1
        if isprime(n):
            return n


def prod(lst):
    '''Returns the elemental products of a list.'''
    p = 1
    for i in lst:
        p *= i
    return p


def findnth(string, sub, n):
    '''Returns index of the nth occurence of sub in string'''
    start = string.find(sub)
    while start >= 0 and n > 1:
        start = string.find(sub, start + 1)
        n -= 1
    return start


arab_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


def roman2int(s: str):
    """Converts roman numeral to arabic numeral."""
    roman_arab = {x: y for y, x in arab_roman.items()}
    s = s.upper()
    (i, num) = (0, 0)
    while i < len(s):
        a, b = (s[i], s[i:i+2])
        if b not in roman_arab:
            num += roman_arab[a]
            i += len(a)
        else:
            num += roman_arab[b]
            i += len(b)
    return num


def int2roman(num: int):
    """Converts arabic numeral to roman numeral."""
    x = ''
    for i, r in arab_roman.items():
        n = num // i
        if n > 0:
            x += n * r
            num %= i
    return x


def partitions(arr):
    """Generates all possible partitions of an array"""
    n = len(arr)
    for partition_index in range(2 ** (n - 1)):
        # current partition, e.g., [['a', 'b'], ['c', 'd', 'e']]
        partition = []
        # used to accumulate the subsets, e.g., ['a', 'b']
        subset = []
        for position in range(n):
            subset.append(arr[position])
            # check whether to "break off" a new subset
            if 1 << position & partition_index or position == n - 1:
                partition.append(subset)
                subset = []
        yield partition


def isorted(A, key=1):
    """Returns True if an array is sorted. Use key=1 for ascending and key=2 for descending"""
    length = len(A)
    if length == 1:
        return True
    if key == 1:
        for i in range(1, length):
            if A[i-1] > A[i]:
                return False
        return True
    else:
        for i in range(1, length):
            if A[i-1] < A[i]:
                return False
        return True


def find(arr, condition=lambda x: bool(x)):
    """Find all elements in an array that satisfy the condition given by a boolean function"""
    b = (i for i in arr if condition(i))
    return b
