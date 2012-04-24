def collatzlen(n):
    l = collatzlen.memo.get(n, None)
    if l is not None: return l
    if n == 1:
        ret = 1
    elif n % 2 == 0:
        ret = 1+collatzlen(n/2)
    else:
        ret = 1+collatzlen(3*n+1)
    collatzlen.memo[n] = ret
    return ret
collatzlen.memo = {}


m = 0
besti = 0
for i in range(500000,1000000):
    c = collatzlen(i)
#    print i, c
    if c > m:
        besti = i
        m = c
print besti

