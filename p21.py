from sets import Set
from eulertools import sieve, cachesumdiv
divisors = list(sieve(10000))
primes = Set(sieve(10000))

sumdivisors = lambda n: cachesumdiv(n, divisors)-n
amicable = []
skips = Set()
for n in range(1,10000):
    if n in skips or n in primes: continue
    sn = sumdivisors(n)
    if sn <= 10000 and sn != n and sumdivisors(sn) == n:
        amicable.append(n+sn)
        skips.add(sn)
print sum(amicable)
