from sets import ImmutableSet, Set
from itertools import chain
digits = ImmutableSet((1,2,3,4,5,6,7,8,9))
n2d = lambda n: map(int, str(n))
d2n = lambda tup: reduce(lambda a,b: 10*a+b, tup, 0)
# the product of m and n will have at least max(len(digits(m)), len(digits(n))) digits, and the number of digits of m, n, and m*n must be 9. The product must be four digits long, since no 1/3 or 2/2 digit number pairs multiply to a five digit number, no 1/5, 2/4, 3/3 to a three digit number. There are 1/4 and 2/3 pairs that multiply to four digit numbers.
def permute_n(seq, n):
    if not seq or not n: return
    if n == 1:
        for s in seq:
            yield (s,)
        return
    for p in permute_n(seq[1:], n-1):
        for i in range(n):
            yield p[:i]+(seq[0],)+p[i:]
    for p in permute_n(seq[1:],n):
        yield p
possiblemultiples = ((d2n(t), ImmutableSet(t)) for t in permute_n(tuple(digits), 4))

def test(n,digs):
    candidates = digits - digs
    candidatesl = tuple(candidates)
    def makesproduct(x):
        xset = ImmutableSet(n2d(x))
        d, m = divmod(n,x)
        dset = ImmutableSet(n2d(d))
        if 0 in dset: return False
        if m == 0 and len(dset) + len(xset) + len(digs) == 9 and dset - digs - xset == dset:
            return True
    if len(digs) == 4:
        # 2 and 3, and 1 and 4
        twodigits = (d2n(t) for t in permute_n(candidatesl, 2))
        if any(makesproduct(t) for t in twodigits):
            return True
        if any(makesproduct(t) for t in candidatesl):
            return True
pandigitals = Set()
for (n, ds) in possiblemultiples:
    if test(n,ds):
        pandigitals.add(n)
print sum(pandigitals)
