from eulertools import sieve, isprime, permute
primes = list(sieve(31622))
tonum = lambda ds: reduce(lambda a,b :10*a+b, ds, 0)

def main():
    for i in range(9, 2, -1):
        digits = range(i,0,-1)
        pandigitals = permute(tuple(digits))
        for p in pandigitals:
            if p[-1] % 2 == 0: continue
            t = tonum(p)
            if isprime(t, primes):
                print t
                return
if __name__ == '__main__': main()
