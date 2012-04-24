from sets import Set, ImmutableSet

def subsets(s):
    '''
The subsets of a set S with initial element e are:
The subsets of S - {e} (incl. empty set)
For each of those subsets s, s + {e}
S
    '''
    if not s:
        yield Set()
        return
    e = Set([s.pop()])
    for ss in subsets(s):
        yield ss
        yield ss.union(e)

def disjointsubsets(s):
    for ss1 in subsets(s.copy()):
        for ss2 in subsets(s-ss1):
            if ss1 and ss2:
                yield (ss1, ss2)

def special(s):
    for (ss1,ss2) in disjointsubsets(s):
        if len(ss1) > len(ss2) and sum(ss1) <= sum(ss2): return False
        if sum(ss1) == sum(ss2): return False
    return True

def main():
    tot = 0
    for line in open("sets.txt").read().split('\n'):
        line = line.strip()
        if not line: continue
        s = Set(int(w) for w in line.split(','))
        if special(s): tot += sum(s)
    print tot
if __name__ == '__main__': main()
