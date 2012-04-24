from eulertools import sieve, isprime
from sets import Set
primes = Set(sieve(1000000))

def rotate(n):
    toint = lambda ds: reduce(lambda a,b: 10*a+b, ds, 0)
    digits = [int(c) for c in str(n)]
    rotations = len(digits) - 1
    for i in range(rotations):
        digits = digits[1:] + [digits[0]]
        yield toint(digits)
seen = Set()
for p in primes:
    if p in seen: continue
    rotations = list(rotate(p))
    for r in rotations:
        if r not in primes:
            break
    else:
        seen.add(p)
        seen.update(rotations)
print len(seen)
