import math, itertools

digits = lambda x: math.floor(math.log(x,10)+1)
count = 0
for exp in itertools.count(1):
  print "try %d..." % exp
  foundone = False
  for i in range(1,9):
    if i == 10: continue
    powd = i**exp
    d = digits(powd)
    if exp == d:
      count += 1
      if not foundone:
        print "found one for exp == %d: %d**%d == %d" % (exp,i,exp,powd)
      foundone = True
    elif d > exp:
      break
  if exp == 23: break
print count
