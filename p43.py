from itertools import *
from sets import Set
seventeens = []
c = count(1)
for x in c:
    m = 17*x
    if m > 1000:
        break
    if m < 100:
        seventeens.append([0]+map(int, str(m)))
    else:
        seventeens.append(map(int, str(m)))
svntns = [svnt for svnt in seventeens if len(Set(svnt)) == 3]
thrtns=[]
elvs = []
sevs = []
fivs = []
thrs = []
twos = []
ones = []
def test(modulo, source, result):
    for x in range(0,10):
        for s in source:
            if x not in s:
                if (100*x + 10*s[0] + s[1]) % modulo == 0:
                    result.append([x]+s)
test(13, svntns, thrtns)
test(11, thrtns, elvs)
test(7, elvs, sevs)
test(5, sevs, fivs)
test(3, fivs, thrs)
test(2, thrs, twos)
test(1, twos, ones)
added = []
print sum([reduce(lambda a,b: 10*a+b, one, 0) for one in ones])
