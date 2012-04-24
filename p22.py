data = sorted(eval('[%s]'%open("names.txt").read().strip()))
score = lambda nm: sum([ord(c)-64 for c in nm])
print reduce(lambda d,(i,e): d+(1+i)*score(e), enumerate(data), 0)
    
