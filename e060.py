# Problem 60: Prime pair sets
from myfunc import primes, array2num, isprime


def array2num(lst):
    '''Converts array to digits'''
    return int(''.join(str(num) for num in lst))


p = primes(10000)
p.remove(2)
p.remove(5)
limit = len(p)
found = False
for a in range(limit-4):
    for b in range(1, limit-3):
        ab = array2num((p[a], p[b]))
        ba = array2num((p[b], p[a]))
        if isprime(ab) and isprime(ba):
            for c in range(2, limit-2):
                ac = array2num((p[a], p[c]))
                ca = array2num((p[c], p[a]))
                bc = array2num((p[b], p[c]))
                cb = array2num((p[c], p[b]))
                if isprime(ac) and isprime(ca) \
                   and isprime(bc) and isprime(cb):
                    for d in range(3, limit-1):
                        ad = array2num((p[a], p[d]))
                        da = array2num((p[d], p[a]))
                        bd = array2num((p[b], p[d]))
                        db = array2num((p[d], p[b]))
                        cd = array2num((p[c], p[d]))
                        dc = array2num((p[d], p[c]))
                        if isprime(ad) and isprime(da) and isprime(bd) \
                           and isprime(db) and isprime(cd) and isprime(dc):
                            for e in range(4, limit):
                                ae = array2num((p[a], p[e]))
                                ea = array2num((p[e], p[a]))
                                be = array2num((p[b], p[e]))
                                eb = array2num((p[e], p[b]))
                                ce = array2num((p[c], p[e]))
                                ec = array2num((p[e], p[c]))
                                de = array2num((p[d], p[e]))
                                ed = array2num((p[e], p[d]))
                                if isprime(ae) and isprime(ea) and isprime(be) \
                                   and isprime(eb) and isprime(ce) and\
                                   isprime(ec) and isprime(de) and isprime(ed):
                                    found = True
                                    break
                            if found:
                                break
                    if found:
                        break
            if found:
                break
    if found:
        break
G = (p[a], p[b], p[c], p[d], p[e])
print(sum(G))
