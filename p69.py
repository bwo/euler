import itertools
def erat2( ):
    D = {  } 
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
primes = erat2

def totient(lim):
    tots = [1] * (lim+1)
    for p in primes():
        if p > lim: break
        tots[p] = p - 1
        for i in range(2,1+lim/p):
            j = p * i
            while i % p == 0:
                tots[j] *= p
                i /= p
            tots[j] *= (p-1)
    return tots

if __name__ == '__main__':
    ratios = [(float(i)/t,i) for (i,t) in enumerate(totient(1000000))]
    print max(ratios)[1]
