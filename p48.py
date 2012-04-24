tendigits = 10000000000
s = 0
for x in range(1,1001):
    s += pow(x,x,tendigits)
print s % tendigits
