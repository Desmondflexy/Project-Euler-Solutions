with open('p096_sudoku.txt', 'r') as f:
    data = f.read().splitlines()

sudoku = {x: [] for x in range(50)}
for line in range(len(data)):
    s = line // 10
    if line % 10 != 0:
        sudoku[s].append(list(data[line]))


def getzeros():
    global possibilities
    while True:
        flag = True
        zeros = []
        possibilities = []
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if mat[i][j] == '0':
                    possible = getpossibilities([i, j])
                    if len(possible) == 1:
                        mat[i][j] = possible[0]
                        flag = False
                    else:
                        zeros.append((i, j))
                        possibilities.append(possible)
        if flag:
            break
    return zeros


def getpossibilities(p):
    possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    j = p[1]
    for i in range(9):
        if mat[i][j] in possible:
            possible.remove(mat[i][j])

    i = p[0]
    for j in range(9):
        if mat[i][j] in possible:
            possible.remove(mat[i][j])

    for i in range((p[0] // 3) * 3, (p[0] // 3) * 3 + 3):
        for j in range((p[1] // 3) * 3, (p[1] // 3) * 3 + 3):
            if mat[i][j] in possible:
                possible.remove(mat[i][j])
    return possible


def solve(idx):
    if idx >= len(zeros):
        return True
    r, c = zeros[idx]
    for num in possibilities[idx]:
        mat[r][c] = str(num)
        if not isvalid(r, c, num):
            continue
        if solve(idx + 1):
            return True
    mat[r][c] = 0
    return False


def isvalid(r, c, num):
    for i in range(9):
        if mat[r][i] == str(num) and i != c:
            return False
    for i in range(9):
        if mat[i][c] == str(num) and i != r:
            return False
    ti, tj = (r // 3) * 3, (c // 3) * 3
    for i in range(ti, ti + 3):
        for j in range(tj, tj + 3):
            if mat[i][j] == str(num) and (i, j) != (r, c):
                return False
    return True


solution = 0
for n in range(50):
    mat = sudoku[n]

    zeros = getzeros()
    solve(0)
    solmat = str(mat[0][0]) + str(mat[0][1]) + str(mat[0][2])
    solution += int(solmat)

print(solution)
