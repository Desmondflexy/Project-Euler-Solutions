def MinWindowSubstring(strArr):

    def hasAllx(a: str, b: str) -> bool:
        """Checks if string a has all characters in string b"""
        A = list(a)
        B = list(b)
        for x in a:
            if x in B:
                B.remove(x)
                A.remove(x)
        return len(B) == 0

    (N, k) = strArr
    min_len_N = 50
    strArr = ''
    for i in range(0, len(N)-1):
        for j in range(i+len(k)-1, len(N)):
            subN = N[i:j+1]
            if hasAllx(subN, k):
                if len(subN) < min_len_N:
                    min_len_N = len(subN)
                    strArr = subN
    return strArr


print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
