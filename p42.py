from sets import Set
def triangles():
    i = 1
    while 1:
        yield (i*i+i)/2
        i += 1
triset = Set()
ts = triangles()
[triset.add(ts.next()) for _ in range(100)]
words = eval(open('words.txt').read())
w2n = lambda w: reduce(lambda a,b: a+ord(b)-64, w, 0)
count = 0
for w in words:
    if w2n(w) in triset:
        count += 1
print count
