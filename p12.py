from eulertools import sieve
from itertools import count
from operator import mul
from collections import defaultdict
primes = list(sieve(1000000))

def divisors(n):
    def _numdivisors(n, acc):
        if n == 1: return acc
        for p in primes:
            if n % p == 0:
                while n % p == 0:
                    acc[p] += 1
                    n /= p
                return _numdivisors(n,acc)
    c = divisors.cache.get(n, None)
    if c: return c
    d= _numdivisors(n,defaultdict(lambda: 1))
    if not d: d = 1
    else: d = reduce(mul, d.values())
    divisors.cache[n] = d
    return d
divisors.cache = {}

def tridivisors(i):
    if i % 2 == 0:
        di = divisors(i/2) 
        diplus = divisors(i+1)
    else:
        di = divisors(i)
        diplus = divisors((i+1)/2)
    return diplus*di

for i in count(1):
    if tridivisors(i) > 500:
        print (i*i+i)/2
        break
