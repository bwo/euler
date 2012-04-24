from operator import add
digsum = lambda n: reduce(add, map(int, str(n)), 0)
m = 0
for a in range(1,100):
    for b in range(1,100):
        m = max(m, digsum(a**b))
print m
