# coding: utf-8
import time
import random


DIRS = {(0, 1): 'right', (1, 0): 'down', (0, -1): 'left', (-1, 0): 'up'}


def cheapest_path_fast(grid, start, finish):
    h, w = len(grid), len(grid[0])
    prev, bag = {start: None}, {start: 0}
    while bag:
        print(bag)
        x, y = pos = min(bag, key=bag.get)
        if pos == finish:
            break
        cost = bag.pop(pos) + grid[x][y]
        for u, v in DIRS:
            new_pos = m, n = x + u, y + v
            if not (0 <= m < h and 0 <= n < w):
                continue
            if new_pos in prev and new_pos not in bag:
                continue
            if cost < bag.get(new_pos, float('inf')):
                bag[new_pos], prev[new_pos] = cost, pos
    path = []
    while pos != start:
        (x1, y1), (x0, y0) = pos, prev[pos]
        path.append(DIRS[x1 - x0, y1 - y0])
        pos = prev[pos]
    return path[::-1]


t = [[1, 9, 1], [2, 9, 1], [2, 1, 1]]

begin = time.time()
print(cheapest_path_fast(t, (0, 0), (0, 2)))
print(time.time()-begin)

tt = []
for j in range(30):
    tt.append([random.random() for e in range(40)])
'''
begin = time.time()
print(cheapest_path_fast(tt, (10, 9), (19, 20)))
print(time.time()-begin)
'''
