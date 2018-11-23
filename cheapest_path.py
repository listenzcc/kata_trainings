# coding: utf-8


def cheapest_path(t, start, finish):
    cutdict = cut_tdict(t)

    results = dict()

    path = []
    path.append(start)

    score = [0]

    go(t, finish, path.copy(), score.copy(), results, cutdict)

    c = min(list(e for e in results))

    good_path = results[c]

    leads = []
    for j in range(1, len(good_path)):
        diff = (good_path[j][0]-good_path[j-1][0],
                good_path[j][1]-good_path[j-1][1])
        leads.append(direct(diff))

    return leads


def cut_tdict(t):
    x = len(t)
    y = len(t[0])
    cutdict = dict()
    for j in range(x):
        for k in range(y):
            cutdict[(j, k)] = -1
    return cutdict


def go(t, finish, path, score, results, cutdict):
    last = path[-1]
    score[0] += t[last[0]][last[1]]

    if cutdict[last] == -1:
        cutdict[last] = score[0]

    if cutdict[last] < score[0]:
        return

    if last == finish:
        results[score[0]] = path
        return

    n = nexts(path, t)
    if n == []:
        return

    for e in n:
        p = path.copy()
        p.append(e)
        go(t, finish, p, score.copy(), results, cutdict)

    return


def nexts(path, t):
    out = []
    this = path[-1]
    for e in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next = (this[0]+e[0], this[1]+e[1])
        if is_next(next, path, t):
            out.append(next)
    return out


def direct(e):
    if e == (1, 0):
        return 'down'
    if e == (-1, 0):
        return 'up'
    if e == (0, 1):
        return 'right'
    if e == (0, -1):
        return 'left'


def is_next(move, path, t):
    if move in path:
        return False
    x = len(t)
    y = len(t[0])
    if move[0] < 0:
        return False
    if move[0] >= x:
        return False
    if move[1] < 0:
        return False
    if move[1] >= y:
        return False
    return True


t = [[1, 9, 1], [2, 9, 1], [2, 1, 1]]
print(cheapest_path(t, (0, 0), (0, 2)))

t = [[1, 19, 1, 1, 1],
     [1, 19, 1, 19, 1],
     [1, 19, 1, 19, 1],
     [1, 19, 1, 19, 1],
     [1, 1, 1, 19, 1]]
print(cheapest_path(t, (0, 0), (4, 4)))

t = [[1, 20, 1, 2, 1, 1, 1, 1, 1, 1],
     [1, 90, 90, 90, 90, 90, 90, 90, 90, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print(cheapest_path(t, (0, 0), (0, 2)))
