from __builtin__ import range as _range
from operator import mul
from collections import defaultdict
import math
import sets


class _stream_iter:
    def __init__(self, s):
        self.stream = s
        self.i = 0
    def next(self):
        try:
            val = self.stream[self.i]
        except IndexError: raise StopIteration
        self.i += 1
        return val

class stream(list):
    def __init__(self, iteratable):
        list.__init__(self)
        self.__it = iter(iteratable)
    def _get_next(self):
        n = self.__it.next()
        self.append(n)
        return n
    def __iter__(self):
        return _stream_iter(self)
    def __getitem__(self, i):
        length=len(self)
        try:
            if i >= length:# or (length == 0 and i >= 0):
                for j in range(i + 1 - length):
                    self._get_next()
            elif i < 0:
                try:
                    while 1:
                        self._get_next()
                except StopIteration:
                    pass
            return list.__getitem__(self, i)
        except (IndexError, StopIteration):
            raise IndexError, 'stream index out of range'
    def __getslice__(self, i, j):
        try:
            junk, junk = self[i], self[j]
        except IndexError:
            pass
        return list.__getslice__(self, i, j)
    def __repr__(self):
        return '<stream instance at 0x%x, %s materialized>' \
               % (id(self), list.__repr__(self))
    def __str__(self):
        return '<stream instance at 0x%x, %s materialized>' \
               % (id(self), list.__str__(self))

class ordered_stream(stream):
    def __init__(self, ible):
        stream.__init__(self, ible)
        self.sofar = sets.Set()
    def _get_next(self):
        n = stream._get_next(self)
        self.sofar.add(n)
        return n
    def __contains__(self, sought):
        if not self.sofar:
            self._get_next()
        if sought in self.sofar:
            return True
        if sought < max(self.sofar):#list.__getitem__(self, -1):
            return False
        try:
            while 1:
                x = self._get_next()
                if sought < x:
                    break
        except StopIteration:
            return sought == x
        last = max(self.sofar)#list.__getitem__(self, -1)
        return last == sought
        
def makestream(g):
    return stream(g())

def makeostream(g):
    return ordered_stream(g())

def fibs():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a+b


def phi():
    a, b = 1, 3
    while 1:
        yield a
        a, b = b, a + b

def primecandidates():
    i = 1
    while 1:
        yield (6*i)-1
        yield (6*i)+1
        i += 1

@makeostream
def primes():
    yield 2
    yield 3
    from math import sqrt
    for i in primecandidates():
        isq = sqrt(i)
        for p in primes:
            if p > isq:
                yield i
                break
            if i % p == 0:
                break
#primes = stream(primes())

def primes2():
    yield 2
    gen = intsfrom(3,2)
    while 1:
        i = gen.next()
        yield i
        gen = difference(gen, intsfrom(i,i))
primes2 = stream(primes2())

def sieve(n):
    sieve = [True]*((n-1)/2) 
    limit = int(math.sqrt(n)/2)
    for i in _range(limit):
        if sieve[i]:
            for j in _range(3*(i+1), (n-1)/2, 2*(i)+3):
                sieve[j] = False
    yield 2
    for (i,s) in enumerate(sieve):
        if s:
            yield 3+i*2

def everyother(seq):
    def switch(_):
        if switch.t:
            switch.t = False
            return True
        switch.t = True
        return False
    switch.t = True
    return splitseq(switch, seq)

def splitseq(f, seq):
    false = []
    true = []
    for item in seq:
        if f(item):
            true.append(item)
        else:
            false.append(item)
    return (true, false)

def sumdiv(n):
    """sumdiv(n)
Return the sum of the divisors of n, an integer."""
    if n == 0: return n
    tot = 1
    count = 0
    for p in primes:
        while n % p == 0:
            count += 1
            n /= p
        if count:
            tot *= (p**(count+1) - 1)/(p-1)
            count = 0
        if n == 1: break
    return tot

def cachesumdiv(n,primes):
# primes is a list of primes
    if n == 0: return n
    def csumdiv_i(n,pindex):
        if n == 1: return 1
        n_o = n
        count = 0
        p = primes[pindex]
        while n % p != 0:
            pindex += 1
            p = primes[pindex]
        while n % p == 0:
            count += 1
            n /= p
        c2 = (p**(count+1)-1)/(p-1)
        c = c2 * csumdiv_i(n,pindex)
        cachesumdiv.cache[n_o] = c
        cachesumdiv.cache[p**count] = c2
        return c
    c = cachesumdiv.cache.get(n)
    if c: return c
    return csumdiv_i(n,0)
cachesumdiv.cache={}

def sumproperdiv(n):
    return sumdiv(n) - n
def cachesumproperdiv(n):
    return cachesumdiv(n) - n

def permute(seq):
    try:
        hash(seq)
    except:
        return permute_nohash(seq)
    else:
        return permute_hash(seq)

def permute_nohash(seq):
    if len(seq) <= 1: yield seq
    else:
        for i in range(len(seq)):
            for p in permute_nohash(seq[:i]+seq[i+1:]):
                yield [seq[i]]+p
        

def permute_hash(seq):
    ##to decrease insane cache size, this computes the permutations based on
    ##the first sequence of any equivalence class of sequences it's called with.
    ##That is, if you call permute_hash((1,2,5,3)), then whenever you call it with
    ##some permutation of (1,2,5,3), you'll get the results back in the order
    ##you got them back the first time.
    ##Cache size is still likely to be insane.
    lseq = list(seq)
    lseq.sort()
    sort_seq = tuple(lseq)
    done = False
    c = permute_hash.cache.get(sort_seq)
    if c:
        for e in c: yield e
        done = True
    if not done:
        if len(seq) <= 1:
            permute_hash.cache[sort_seq] = (seq,)
            yield seq
        else:
            permute_hash.cache[sort_seq] = []
            for i in range(len(seq)):
                for p in permute_hash(seq[:i]+seq[i+1:]):
                    r = (seq[i],)+p
                    permute_hash.cache[sort_seq].append(r)
                    yield r
permute_hash.cache = {}

def intsfrom(start, step=1):
    while 1:
        yield start
        start += step

def difference(a, b):
    '''Yield the elements of a not in b.

Assumes that both a and b are ordered, with no duplicates.'''
    a0, b0 = a.next(), b.next()
    while 1:
        if a0 < b0:
            yield a0
            a0 = a.next()
        elif a0 == b0:
            a0 = a.next()
            b0 = b.next()
        elif a0 > b0:
            b0 = b.next()

def merge(a, b):
    '''Merge the elements of a and b.

Assumes that both a and b are ordered, with no duplicates.'''
    x, y = a.next(), b.next()
    while 1:
        if x < y:
            yield x
            x = a.next()
        elif x == y:
            yield x
            x = a.next()
            y = b.next()
        elif x > y:
            yield y
            y = b.next()

def mergen(a,*bs):
    assert len(bs)
    for i in reduce(merge, bs, a): yield i

def divisorsd(n):
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
    divisorsd.cache[n] = d
    return d
divisorsd.cache = {}


def conjoin(fs):
    l = len(fs)
    if not l: yield []
    elif l == 1:      #special case
        for i in fs[0]():
            yield [i]
    else:
        for first in fs[0]():
            for rest in conjoin(fs[1:]):
                yield [first] + rest

def fast_conjoin(seqs):
    def by_threes(seqs):
        if not seqs:
            yield []
        else:
            results = [None, None, None]
            for results[0] in seqs[0]():
                for results[1] in seqs[1]():
                    for results [2] in seqs[2]():
                        for rest in by_threes(seqs[3:]):
                            yield results + rest
    l = len(seqs)
    if l == 0:
        yield []
        return
    else:
        l %= 3
        if l == 0:
            for x in by_threes(seqs):
                yield x #damn there is no easier way to express this!
        elif l == 1:
            for first in seqs[0]():
                first = [first]
                for rest in by_threes(seqs[1:]):
                    yield first + rest
        elif l == 2:
            s2 = [None, None]
            for s2[0] in seqs[0]():
                for s2[1] in seqs[1]():
                    for rest in by_threes(seqs[2:]):
                        yield s2 + rest

def divisors(n,primes):
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
    d= _numdivisors(n,defaultdict(lambda: 1)) or {}
#    if not d: d = 1
#    else: d = reduce(mul, d.values())
    divisors.cache[n] = d
    return d
divisors.cache = {}

def isprime(n, primes):
    nsq = int(math.sqrt(n))
    if n == nsq * nsq: return False
    for p in primes:
        if nsq < p: return True
        if n == p: return True
        if n % p == 0: return False
    return True
