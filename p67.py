data = open("triangle.txt").read()
triangle = []
for line in data.split("\n"):
    if not line: continue
    triangle.append([int(w) for w in line.strip().split(' ')])
while len(triangle) > 1:
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i+1])
    del triangle[-1]
print triangle[0][0]
