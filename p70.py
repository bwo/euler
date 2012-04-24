from math import log10
from eulertools import sieve

limit = 10 ** 7
primes = set(sieve(limit))

def totients():
    tots = [1] * (limit+1)
    for p in primes:
        tots[p] = p - 1
        for i in range(2,1+limit/p):
            j = p * i
            while i % p == 0:
                tots[j] *= p
                i /= p
            tots[j] *= (p-1)
    return tots
    
def isperm(n, m):
#    if not -1 < int(log10(n)) - int(log10(m)) < 1: return False
    s = str(n)
    t = list(str(m))
    if len(s) != len(t): return False
    ## surprisingly, this is faster than sorted(str(n)) == sorted(str(m))
    ## there's an O(n) method too, which is also slower than this.
    try:
        for c in s:
            t.remove(c)
    except ValueError:
        return False
    return not t

if __name__ == '__main__':
    totlist = totients()
    perms = ((i,t) for (i,t) in enumerate(totlist) if i > 1 and isperm(i,t))
    minperm = (None, None)
    for (n, tot_n) in perms:
#        if n == 1: continue
        lastmin = minperm[0]
        ratio = float(n)/tot_n
        if lastmin is None or ratio < lastmin:
            minperm = (ratio, n)
    print minperm[1]
