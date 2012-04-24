from eulertools import sieve
from sets import ImmutableSet as Set
from collections import defaultdict
d = defaultdict(lambda: [])
digits = lambda n: [int(c) for c in str(n)]
primes = [x for x in sieve(10000) if x > 1000]
digitset = [Set(digits(p)) for p in primes]
for (p,dig) in zip(primes,digitset):
##    if len(dig) == 4:
    d[dig].append(p)
exclude = (1487, 4817, 8147)
for (p,dig) in zip(primes, digitset):
    if len(d[dig]) >= 3:
        ps = sorted(d[dig])
        while ps:
            p, ps = ps[0], ps[1:]
            for p2 in ps:
                if 2*p2-p in ps:
                    print "%s%s%s" % (p, p2, 2*p2-p)
