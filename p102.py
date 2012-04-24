import math

def lensq((a,b), (x,y)):
    return (x-a)**2 + (y-b)**2

def angle(v, a, b):
    ab2 = lensq(a,b)
    va2 = lensq(v,a)
    vb2 = lensq(v,b)
    return math.acos((ab2 - va2 - vb2)/(-2 * math.sqrt(vb2) * math.sqrt(va2)))

def containspoint(triangle, pt):
    a, b, c = triangle
    ct = 0
    if a == pt or b == pt or c == pt: return True
    for (v, (o1,o2)) in [(a, (b,c)), (b, (a,c)), (c, (a,b))]:
        o1vo2 = angle(v, o1, o2)
        ptvo2 = angle(v, pt, o2)
        ptvo1 = angle(v, o1, pt)
        if ptvo1 > o1vo2 or ptvo2 > o1vo2:
            return False
    return True
        
        
containso = lambda triangle: containspoint(triangle, (0,0))

def main():
    triangles = []
    for line in open("triangles.txt").read().strip().split('\n'):
        if not line: continue
        a, b, c, d, e, f = map(int, line.split(','))
        triangles.append(((a,b), (c,d), (e,f)))
    print len(filter(containso, triangles))
if __name__ == '__main__': main()
