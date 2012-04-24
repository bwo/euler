import genlib, math

targ=600851475143L
m=0
for p in genlib.primes:
  if p > targ: break
  if targ % p == 0:
    targ = targ / p
    m = p

print m
