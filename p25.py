import eulertools
big = 10**999
count = 0
for f in eulertools.fibs():
    if f / big != 0:
        print count
        break
    count += 1
