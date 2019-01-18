# code: utf-8


def solve(clues):
    print(clues)
    print('='*60)
    shift = []
    for c in clues[1]:
        shift.append(0)
        for e in range(len(c)-1):
            shift.append(1)

    grid = mkgrid(shift, clues)
    is_valid(grid, clues, debug=True)
    guess(shift, clues)


old = set()


def guess(shift, clues):
    t = tuple(shift)
    if t in old:
        return False
    old.add(t)
    # print(shift)
    grid = mkgrid(shift, clues)
    if is_good_ans(grid, clues):
        print(grid)
        return True
    return is_valid(grid, clues) and any(guess(sj, clues) for sj in list(plus_one(shift, j) for j in range(len(shift))))
    # return max(shift) < 3 and any(guess(sj, clues) for sj in list(plus_one(shift, j) for j in range(len(shift))))


def plus_one(shift, j):
    sj = shift.copy()
    sj[j] += 1
    return sj


def mkgrid(shift, clues):
    sc = shift.copy()
    sc.reverse()
    grid = list([] for j in range(len(clues[1])))
    for j, e in enumerate(clues[1]):
        for ee in e:
            grid[j] += list(0 for k in range(sc[-1]))
            sc.pop()
            grid[j] += list(1 for k in range(ee))
        while len(grid[j]) < 5:
            grid[j].append(0)
    return grid


def is_valid(grid, clues, debug=False):
    if debug:
        print('-'*20, 'is_valid', '-'*20)
        print(shift)
        for j, e in enumerate(clues[1]):
            print('%3d' % j, '%8s' % str(e), grid[j])
    return not max(len(e) for e in grid) > len(grid)


def is_good_ans(grid, clues):
    # print('-'*20, 'is_good_ans', '-'*20)
    for j in range(len(grid)):
        col = list(grid[k][j] for k in range(len(grid)))
        s = ''.join(str(x) for x in col).replace('0', ' ').split()
        length = [len(e) for e in s]
        # print(col, end=': ')
        # print(clues[0][j], tuple(length))
        if not clues[0][j] == tuple(length):
            return False
    return True


clues = (((1, 1), (4,), (1, 1, 1), (3,), (1,)),
         ((1,), (2,), (3,), (2, 1), (4,)))

ans = ((0, 0, 1, 0, 0),
       (1, 1, 0, 0, 0),
       (0, 1, 1, 1, 0),
       (1, 1, 0, 1, 0),
       (0, 1, 1, 1, 1))

print(is_good_ans(ans, clues))

shift = [0, 0, 0, 0, 2, 2]

print(is_valid(mkgrid(shift, clues), clues))

solve(clues)
