def fac(n):
    r = fac.memo.get(n,None)
    if not r:
        if n == 1: r = 1
        else:      r = n*fac(n-1)
        fac.memo[n] = r
    return r
fac.memo = {}

print fac(40)/(fac(20)*fac(20))
