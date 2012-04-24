from eulertools import sieve, cachesumdiv, fast_conjoin as conjoin
from sets import Set
from itertools import count
primes = list(sieve(29000))
sumdivs = lambda n: cachesumdiv(n, primes)

def abundants():
    for i in count(1):
        if i > 28123: break
        sd = sumdivs(i) - i
        if sd > i:
            yield i

abundants = list(abundants())
possibilities = [False]*28124
for i in abundants:
    for j in abundants:
        if i + j > 28123: break
        possibilities[i+j] = True
sum = 0
for i in range(len(possibilities)):
    if not possibilities[i]: sum += i
print sum
