# code: utf-8


from itertools import groupby
from collections import defaultdict

POS, B = defaultdict(set), 5  # 15
f = "{:0>" + str(B) + "b}"
for n in range(1 << B):
    s = f.format(n)
    POS[tuple(sum(1 for _ in g)
              for k, g in groupby(s) if k == '1')].add(tuple(map(int, s)))


def solve(clues):
    clues = {'V': clues[0], 'H': clues[1]}
    grid = {(d, z): list(POS[clues[d][z]]) for d in 'VH' for z in range(B)}

    changed = True
    while changed:
        changed = False

        for x in range(B):
            for y in range(B):

                tupH, iH, tupV, iV = ('H', x), y, ('V', y), x
                if len(grid[tupH]) == 1 and len(grid[tupV]) == 1:
                    continue

                vH = {v[iH] for v in grid[tupH]}
                vV = {v[iV] for v in grid[tupV]}
                target = vH & vV

                if len(vH) == 2 and len(target) == 1:
                    changed = True
                    grid[tupH] = [t for t in grid[tupH] if t[iH] in target]

                if len(vV) == 2 and len(target) == 1:
                    changed = True
                    grid[tupV] = [t for t in grid[tupV] if t[iV] in target]

    return tuple(grid[('H', n)][0] for n in range(B))


clues = (
    (
        (4, 3), (1, 6, 2), (1, 2, 2, 1, 1), (1, 2, 2, 1, 2), (3, 2, 3),
        (2, 1, 3), (1, 1, 1), (2, 1, 4, 1), (1, 1, 1, 1, 2), (1, 4, 2),
        (1, 1, 2, 1), (2, 7, 1), (2, 1, 1, 2), (1, 2, 1), (3, 3)
    ), (
        (3, 2), (1, 1, 1, 1), (1, 2, 1, 2), (1, 2, 1, 1, 3), (1, 1, 2, 1),
        (2, 3, 1, 2), (9, 3), (2, 3), (1, 2), (1, 1, 1, 1),
        (1, 4, 1), (1, 2, 2, 2), (1, 1, 1, 1, 1,
                                  1, 2), (2, 1, 1, 2, 1, 1), (3, 4, 3, 1)
    )
)

clues = (((1, 1), (4,), (1, 1, 1), (3,), (1,)),
         ((1,), (2,), (3,), (2, 1), (4,)))


solve(clues)
