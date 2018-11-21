# coding: utf-8


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    return solve(puzzle)
    return False


def solve(puzzle):
    # printpuzzle(puzzle)
    z = first_zero(puzzle)
    if z == -1:
        return puzzle
    x, y = z[0], z[1]
    newpuzzle = deepcopy(puzzle)
    for e in range(1, 10):
        newpuzzle[x][y] = e
        if is_good_puzzle(newpuzzle, x, y):
            s = solve(newpuzzle)
            if s == -1:
                continue
            return s
    return -1


def deepcopy(puzzle):
    out = []
    for e in puzzle:
        out.append(e.copy())
    return out


def first_zero(puzzle):
    for j in range(9):
        for k in range(9):
            if puzzle[j][k] == 0:
                return (j, k)
    return -1


def is_good_puzzle(puzzle, x, y):
    # determin if the puzzle is legal
    p = puzzle[x][y]
    assert(p > 0)

    # line should contains no conflict
    for j in range(9):
        if j == x:
            continue
        if puzzle[j][y] == p:
            return False

    # colomn should contains no conflict
    for k in range(9):
        if k == y:
            continue
        if puzzle[x][k] == p:
            return False

    # zone should contains no conflict
    zone_grid, zone_dict = zone_33()
    zone_id = zone_dict[(x, y)]
    for e in zone_grid[zone_id]:
        if e == (x, y):
            continue
        if puzzle[x][y] == puzzle[e[0]][e[1]]:
            return False

    return True


def zone_33():
    # each zone grid contains nine (x, y)s
    zone_grid = []
    for j in range(9):
        zone_grid.append([])
    # dict shows (x, y) belongs to which zone
    zone_dict = dict()

    for j in range(0, 3):
        for k in range(0, 3):
            zone_grid[0].append((j, k))
            zone_dict[(j, k)] = 0
        for k in range(3, 6):
            zone_grid[1].append((j, k))
            zone_dict[(j, k)] = 1
        for k in range(6, 9):
            zone_grid[2].append((j, k))
            zone_dict[(j, k)] = 2

    for j in range(3, 6):
        for k in range(0, 3):
            zone_grid[3].append((j, k))
            zone_dict[(j, k)] = 3
        for k in range(3, 6):
            zone_grid[4].append((j, k))
            zone_dict[(j, k)] = 4
        for k in range(6, 9):
            zone_grid[5].append((j, k))
            zone_dict[(j, k)] = 5

    for j in range(6, 9):
        for k in range(0, 3):
            zone_grid[6].append((j, k))
            zone_dict[(j, k)] = 6
        for k in range(3, 6):
            zone_grid[7].append((j, k))
            zone_dict[(j, k)] = 7
        for k in range(6, 9):
            zone_grid[8].append((j, k))
            zone_dict[(j, k)] = 8

    return zone_grid, zone_dict


def printpuzzle(puzzle):
    print('----------:Start')
    for e in puzzle:
        print(e)
    print('----------:Done')


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


'''
zone_grid, zone_dict = zone_33()
printpuzzle(zone_grid)
newpuzzle = deepcopy(puzzle)
for j in range(9):
    for k in range(9):
        newpuzzle[j][k] = zone_dict[(j, k)]
printpuzzle(newpuzzle)
'''

puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
          [0, 0, 0, 4, 0, 6, 0, 0, 0],
          [0, 0, 5, 0, 7, 0, 3, 0, 0],
          [0, 6, 0, 0, 0, 0, 0, 4, 0],
          [4, 0, 1, 0, 6, 0, 5, 0, 8],
          [0, 9, 0, 0, 0, 0, 0, 2, 0],
          [0, 0, 7, 0, 3, 0, 2, 0, 0],
          [0, 0, 0, 7, 0, 5, 0, 0, 0],
          [1, 0, 0, 0, 4, 0, 0, 0, 7]]

sudoku(puzzle)

puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1], [0, 0, 0, 4, 0, 6, 0, 0, 0], [0, 0, 5, 0, 7, 0, 3, 0, 0], [0, 6, 0, 0, 0, 0, 0, 4, 0], [
    4, 0, 1, 0, 6, 0, 5, 0, 8], [0, 9, 0, 0, 0, 0, 0, 2, 0], [0, 0, 7, 0, 3, 0, 2, 0, 0], [0, 0, 0, 7, 0, 5, 0, 0, 0], [1, 0, 0, 0, 4, 0, 0, 0, 7]]

printpuzzle(sudoku(puzzle))

puzzle = [[0, 0, 5, 0, 0, 0, 8, 0, 0], [0, 2, 0, 8, 0, 9, 0, 7, 0], [3, 0, 0, 0, 4, 0, 0, 0, 1], [0, 3, 0, 2, 0, 6, 0, 1, 0], [
    0, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 5, 0, 4, 0, 6, 0], [2, 0, 0, 0, 6, 0, 0, 0, 4], [0, 8, 0, 4, 0, 2, 0, 9, 0], [0, 0, 7, 0, 0, 0, 2, 0, 0]]

printpuzzle(sudoku(puzzle))

puzzle = [[0, 8, 0, 0, 5, 0, 0, 2, 0], [6, 0, 0, 0, 0, 7, 0, 0, 5], [0, 0, 0, 2, 0, 9, 0, 0, 0], [0, 1, 7, 0, 0, 0, 9, 0, 0], [
    5, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 9, 0, 0, 0, 8, 6, 0], [0, 0, 0, 8, 0, 3, 0, 0, 0], [9, 0, 0, 6, 0, 0, 0, 0, 2], [0, 5, 0, 0, 1, 0, 0, 3, 0]]

printpuzzle(sudoku(puzzle))

puzzle = [[0, 0, 3, 2, 0, 0, 0, 0, 4], [0, 2, 0, 0, 9, 0, 0, 6, 0], [8, 0, 0, 0, 0, 5, 1, 0, 0], [6, 0, 0, 0, 0, 7, 4, 0, 0], [
    0, 9, 0, 0, 5, 0, 0, 1, 0], [0, 0, 7, 9, 0, 0, 0, 0, 6], [0, 0, 4, 3, 0, 0, 0, 0, 2], [0, 3, 0, 0, 7, 0, 0, 4, 0], [7, 0, 0, 0, 0, 4, 5, 0, 0]]

printpuzzle(sudoku(puzzle))

puzzle = [[0, 0, 7, 0, 0, 5, 0, 0, 3], [0, 3, 0, 0, 9, 0, 0, 4, 0], [9, 0, 0, 1, 0, 0, 8, 0, 0], [4, 0, 0, 6, 0, 0, 5, 0, 0], [
    0, 7, 0, 0, 3, 0, 0, 1, 0], [0, 0, 5, 0, 0, 9, 0, 0, 6], [0, 0, 4, 0, 0, 7, 0, 0, 2], [0, 8, 0, 0, 2, 0, 0, 5, 0], [2, 0, 0, 8, 0, 0, 4, 0, 0]]

printpuzzle(sudoku(puzzle))
