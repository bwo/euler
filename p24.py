#! /usr/bin/python

import eulertools, itertools
c=0
p = eulertools.permute((0,1,2,3,4,5,6,7,8,9))
while c < 999999:
    p.next()
    c+=1
print p.next()
