from collections import deque


def island_counter(M):
    if M == None or M == [[]]:
        return 0
    islands = 0
    row = len(M)
    col = len(M[0])
    for i in range(0, row):
        for j in range(0, col):
            if M[i][j] == 1:
                islands += 1
            findPartsOfIsland(M, i, j, row, col)
    return islands


def findPartsOfIsland(M, i, j, row, col):
    q = deque()
    q.append((i,j))
    while len(q) != 0:
        i = q.pop()
        x = i[0]
        y = i[1]
        if M[x][y] == 1:
            M[x][y] = 2
            appendIf(q, row, col, x + 1, y)
            appendIf(q, row, col, x - 1, y)
            appendIf(q, row, col, x, y + 1)
            appendIf(q, row, col, x, y - 1)


def appendIf(q, row, col, x, y):
    if x >= 0 and x < row and y >= 0 and y < col:
        q.append((x, y))

M = [[1, 0, 1], [1, 1, 1]]
print island_counter(M)