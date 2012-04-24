from eulertools import fraccycle

m = (7,6) # x, length of cycle
for x in range(9, 999, 2):
    oldx, oldcycle = m
    cycle = len(fraccycle(x))
    if cycle > oldcycle: m = (x, cycle)

print m[0]
