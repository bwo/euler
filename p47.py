from eulertools import sieve, divisors
from itertools import count
primes = list(sieve(10000))
x = 600
while 1:
    if len(divisors(x,primes)) == 4:
        if len(divisors(x+1,primes)) == 4:
            if len(divisors(x+2,primes)) == 4:
                if len(divisors(x+3,primes)) == 4:
                    print x
                    break
                else:  x += 4
            else:  x += 3
        else:  x += 2
    else:  x += 1
