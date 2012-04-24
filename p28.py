from itertools import count
# right 1, down one, left two, up two, 
# right three, down three, left four, up four
# right five, down five, left six, up six

# make the matrix
SIZE=1001
#matrix = []
#for i in range(0,SIZE):
#    matrix.append([1]*SIZE)
x,y = (SIZE/2,SIZE/2) #center
def down():
    i = 1
    while 1:
        yield (2*i-1)
        i += 1
right, down = down().next, down().next
def up():
    i = 1
    while 1:
        yield 2*i
        i += 1
left, up = up().next, up().next
current = count(2).next
tot = 1
done = False
def match(x,y):
    return x == y or (SIZE-x-1 == y)
while not done:
    for i in range(right()):
        c = current()
        x += 1
        if (y,x) == (0, SIZE):
            done = True
            break
        if match(x,y):
            tot += c
    if done: break
    for i in range(down()):
        y += 1
        c = current()
        if match(x,y):
            tot += c
    for i in range(left()):
        x -= 1
        c = current()
        if match(x,y): tot += c
    for i in range(up()):
        y -= 1
        c = current()
        if match(x,y): tot +=c 
print tot
