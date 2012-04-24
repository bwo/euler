def tobinary(x):
    acc = []
    while x:
        if x & 1: acc.append(1)
        else: acc.append(0)
        x >>= 1
    return acc # backwards, but we don't care for this application
def ispal(s):
    ln = len(s)
    for i in range(ln):
        if s[i] != s[ln-i-1]: return False
    return True
c = 0
for i in range(1000000):
    if ispal(str(i)) and ispal(tobinary(i)):
        c += i
print c
