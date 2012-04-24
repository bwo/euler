
matrix = [[131,673,234,103,18],
          [201,96,342,965,150],
          [630,0,746,422,111],
          [538,-400,497,121,956],
          [805,0,524,37,331]]
#matrix = []
#for line in open("matrix.txt").read().split('\n'):
#    if not line: continue
#    matrix.append([int(w) for w in line.split(',')])
sz = len(matrix)
j = sz - 2
#for j in range(sz - 2, -1, -1):
for i in range(sz):
    if i == 0:
        matrix[i][j] += min(matrix[i][j+1],
                            matrix[i+1][j]+matrix[i+1][j+1],
                            matrix[i][j+1]+matrix[i+1][j])
    elif i == sz - 1:
        matrix[i][j] += min(matrix[i][j+1],
                            matrix[i-1][j]+matrix[i-1][j+1],
                            matrix[i][j+1]+matrix[i-1][j+1])
    else:
        matrix[i][j] += min(matrix[i][j+1],
                            matrix[i+1][j]+matrix[i+1][j+1],
                            matrix[i-1][j]+matrix[i-1][j+1])
for j in range(sz - 3, -1, -1):
    print "------"
    print "Column %d" % j
    for row in matrix:
        print row
    for i in range(sz):
        if i == 0:
            matrix[i][j] += min(matrix[i][j+1],
                                matrix[i+1][j]+matrix[i+1][j+1])
        elif i == sz - 1:
            matrix[i][j] += min(matrix[i][j+1],
                                matrix[i-1][j])
        else:
            matrix[i][j] += min(matrix[i][j+1],
                                matrix[i+1][j]+matrix[i+1][j+1],
                                matrix[i-1][j])
print "-----"
for i in range(sz):
    print matrix[i]

print reduce(lambda a, b: min(a,b), [matrix[i][0] for i in range(sz)])

