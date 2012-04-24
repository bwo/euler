def partition(n):
    def p(k,m):
        c = partition.cache.get((k,m))
        if c: return c
        if k > m: return 0
        if k == m: return 1
        c = p(k+1,m)+p(k,m-k)
        partition.cache[(k,m)] = c
        return c
    return p(1,n)-1
partition.cache={}
if __name__ == '__main__':
    print partition(100)
