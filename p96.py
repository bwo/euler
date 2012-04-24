import sudoku

def solve():
    boards = []
    count = 0
    with open('sudoku.txt') as f:
        while count != 50:
            junk = f.readline()
            board = "\n".join([" ".join(f.readline().strip()) for _ in range(9)])
            boards.append(board)
            count += 1
    x = 0
    for board in boards:
        m = sudoku.solve(board)
        x += reduce(lambda acc, i: 10*acc+i, m[0][:3])
    return x

if __name__ == '__main__':
    print solve()
