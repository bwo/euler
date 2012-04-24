from itertools import count
from eulertools import sieve
from sets import Set
primes = Set(sieve(1000))
def triple(a,b,c):
    return a**2 + b**2 == c**2
def gettrips(L):
    for a in range(1,1+L/3):
        for b in range(a+1,(L-a)/2):
            if triple(a, b, L-a-b):
                yield (a,b,L-a-b)
    
def main():
    tested = 0
    candidates = []
    for i in range(500):
        candidates.append([]) # lists of triples.
    for i in range(1,500):
        if i in primes:
            continue
        if candidates[i]:
            continue
        for trip in gettrips(2*i):
            a,b,c = trip
            for multiplier in count(2):
                if i*multiplier >= 500: break
                candidates[i*multiplier].append((a*multiplier, b*multiplier,c*multiplier))
    bestl = 0
    most = 0
    for (i,c) in enumerate(candidates):
        if len(c) > most:
            most = len(c)
            bestl = i
    print 2*bestl

if __name__ == '__main__': main()
