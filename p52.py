from sets import Set
samedigs = lambda a, b: Set(str(a)) == Set(str(b))
for i in range(125874, 166666):
    if samedigs(i, 2*i) and samedigs(3*i, 4*i) and samedigs(5*i, 6*i) and samedigs(i, 3*i) and samedigs(4*i, 5*i):
        print i
        break
