from itertools import count
import sys, math
from eulertools import sieve
from sets import Set
SIZE=99001 # a guess
def evens():
    i = 2
    while 1:
        yield i
        i += 2
primes = list(sieve(SIZE))
def checkprime(n):
    sn = int(math.sqrt(n))
    if sn > SIZE:
        print "too small!"
        sys.exit(0)
    for p in primes:
        if n == p: return 1
        if n % p == 0:
            return 0
    return 1
tot = 1
pcount = 0
i = 1
evens = evens().next
while 1:
    e = evens()
    tot += 4
    i += e
    pcount+=checkprime(i)
    i += e
    pcount+=checkprime(i)
    i += e
    pcount+=checkprime(i)
    i += e # perfect square
    if float(pcount)/tot < .1:
        print pcount, tot, e+1
        break
