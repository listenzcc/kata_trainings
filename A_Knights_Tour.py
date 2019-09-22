# coding: utf-8

'''A Knight's Tour
A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square only once.

https://en.wikipedia.org/wiki/Knight%27s_tour

Traditional chess boards are 8x8 grids, but for this kata we are interested in generating tours for any square board sizes.

You will be asked to find a knight's path for any NxN board from any start position.

I have provided a tool to visualize the output of your code at the following link: http://jsfiddle.net/7sbyya59/2/

EDIT: The expected output is a 2D array (n x 2) comprised of the [x,y] coordinates of the Knight's path taken in sequential order. (e.g. [[2,3],[4,4],...,[x,y]])

All test cases will have a passing solution.'''


import time


def knights_tour_slow(start, size):
    """
    Finds a knight's tour from start position visiting every
    board position exactly once.

    A knight may make any "L" move which is valid in chess. That is:
    any rotation of "up 1 over 2" or "up 2 over 1". The problem
    description has a full explanation of valid moves.

    Arguments:
        start - (row, col) starting position on board.
        size - number of rows in the square board.

    Returns:
        List of positions beginning with the start position
        which constitutes a valid tour of the board; visiting
        each position exactly once.
    """
    legal_moves = [(-1, 2),
                   (-1, -2),
                   (1, 2),
                   (1, -2),
                   (2, 1),
                   (2, -1),
                   (-2, 1),
                   (-2, -1)]

    def is_legal(pos):
        return all([pos[0] > -1,
                    pos[0] < size,
                    pos[1] > -1,
                    pos[1] < size])

    def nexts(pos):
        return set((pos[0]+m[0], pos[1]+m[1])
                   for m in legal_moves
                   if is_legal((pos[0]+m[0], pos[1]+m[1])))

    remain = set((j, k) for j in range(size) for k in range(size))
    remain.remove(start)
    past = [start]
    ss = size * size

    def tour(pos):
        if len(past) == ss:
            return True
        for n in nexts(pos):
            if n in past:
                continue
            past.append(n)
            if tour(n):
                return True
            past.pop()
        return False

    tour(start)
    return past


def knights_tour(start, size):

    _moves = [(-1, 2),
              (-1, -2),
              (1, 2),
              (1, -2),
              (2, 1),
              (2, -1),
              (-2, 1),
              (-2, -1)]

    # _moves = [(-1, 0),
    #           (1, 0),
    #           (0, -1),
    #           (0, 1)]

    _counter = {(j, k): 0 for j in range(size) for k in range(size)}
    _passed = {(j, k): False for j in range(size) for k in range(size)}

    _steps = _counter.copy()
    for j, k in _steps.keys():
        _steps[(j, k)] = set((x, y) for x in range(size)
                             for y in range(size) if (j-x, k-y) in _moves)
        _counter[(j, k)] = len(_steps[(j, k)])

    path = []
    ss = size * size

    def travel(pos):
        if len(path) == ss:
            return True
        # if pos in path:
        #     return False
        if _passed[pos]:
            return False

        path.append(pos)
        _passed[pos] = True
        for n in _steps[pos]:
            _counter[n] -= 1

        if any([travel(s) for s in sorted(_steps[pos], key=lambda e: _counter[e])]):
            return True

        path.pop()
        _passed[pos] = False
        for n in _steps[pos]:
            _counter[n] += 1

        return False

    travel(start)

    return path


def knights_tour_fast(start, size):

    MOVES = [(-2, 1), (-2, -1), (-1, -2), (1, -2),
             (2, -1), (2, 1), (1, 2), (-1, 2)]

    def genNeighs(pos): return ((pos[0]+dx, pos[1]+dy)
                                for dx, dy in MOVES if (pos[0]+dx, pos[1]+dy) in Warnsdorf_DP)

    def travel(pos):
        neighs = sorted((Warnsdorf_DP[n], n) for n in genNeighs(pos))
        for nSubNeighs, neigh in neighs:
            del Warnsdorf_DP[neigh]
            path.append(neigh)
            subNeighs = list(genNeighs(neigh))
            for n in subNeighs:
                Warnsdorf_DP[n] -= 1
            travel(neigh)
            if not Warnsdorf_DP:
                break
            else:
                for n in subNeighs:
                    Warnsdorf_DP[n] += 1
                Warnsdorf_DP[path.pop()] = nSubNeighs

    path, Warnsdorf_DP = [start], {(x, y): 0 for x in range(
        size) for y in range(size) if (x, y) != start}
    for pos in Warnsdorf_DP:
        Warnsdorf_DP[pos] = sum(1 for _ in genNeighs(pos))
    travel(start)

    return path


size = 6
t = time.time()
for start in ((0, 0), (2, 2), (5, 5)):
    print('-' * 80)
    print(start, size)
    past = knights_tour(start, size)
    print(past)
print(time.time() - t)


t = time.time()
for start in ((0, 0), (2, 2), (5, 5)):
    print('-' * 80)
    print(start, size)
    past = knights_tour_fast(start, size)
    print(past)
print(time.time() - t)
