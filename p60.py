from math import log10
from itertools import islice
from eulertools import primes, isprime

memo = {}

def testconcat(p,q):
    p, q = primes[p], primes[q]
    if (p,q) in memo: return memo[(p,q)]
    if not isprime((10**int(1+log10(p)))*q+p, primes) or \
        not isprime((10**int(1+log10(q)))*p+q, primes):
        r = False
    else:
        r = True
    memo[(p,q)] = r
    return r

def testconcats(*ps):
    testers, testee = ps[:-1], ps[-1]
    return all(testconcat(tester, testee) for tester in testers)        

def getfive():
    i = 3
    while True:
        i += 1
        for j in range(i-1, 3, -1):
            if not testconcats(i, j):
                continue
            for k in range(j-1, 2, -1):
                if not testconcats(i, j, k):
                    continue
                for l in range(k-1, 1, -1):
                    if not testconcats(i, j, k, l):
                        continue
                    for m in range(l-1, 0, -1):
                        if not testconcats(i, j, k, l,
                                           m):
                            continue
                        yield (i, j, k, l, m)

                                         
if __name__ == '__main__':
   sums = []
   for x in getfive():
       sums.append(sum(primes[i] for i in x))
       break # we'll just make an assumption...
   print min(sums)

