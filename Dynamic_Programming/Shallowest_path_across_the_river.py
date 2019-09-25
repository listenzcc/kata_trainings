# coding: utf-8

'''Ever heard about Dijkstra's shallowest path algorithm? Me neither. But I can imagine what it would be.

You're hiking in the wilderness of Northern Canada and you must cross a large river. You have a map of one of the safer places to cross the river showing the depths of the water on a rectangular grid. When crossing the river you can only move from a cell to one of the (up to 8) neighboring cells. You can start anywhere along the left river bank, but you have to stay on the map.

An example of the depths provided on the map is

[[2, 3, 2],
 [1, 1, 4],
 [9, 5, 2],
 [1, 4, 4],
 [1, 5, 4],
 [2, 1, 4],
 [5, 1, 2],
 [5, 5, 5],
 [8, 1, 9]]
If you study these numbers, you'll see that there is a path accross the river (from left to right) where the depth never exceeds 2. This path can be described by the list of pairs [(1, 0), (1, 1), (2, 2)]. There are also other paths of equal maximum depth, e.g., [(1, 0), (1, 1), (0, 2)]. The pairs denote the cells on the path where the first element in each pair is the row and the second element is the column of a cell on the path.

Your job is to write a function shallowest_path(river) that takes a list of lists of positive ints (or array of arrays, depending on language) showing the depths of the river as shown in the example above and returns a shallowest path (i.e., the maximum depth is minimal) as a list of coordinate pairs (represented as tuples, Pairs, or arrays, depending on language) as described above. If there are several paths that are equally shallow, the function shall return a shortest such path. All depths are given as positive integers.'''

import time
from pprint import pprint


def shallowest_path(river):
    if len(river[0]) == 1:
        xx = sorted([river[j][0], j] for j in range(len(river)))[0]
        return [(xx[1], 0)]

    river_depth = {(j, k): river[j][k]
                   for j in range(len(river))
                   for k in range(len(river[0]))}

    move = [(0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)]

    def genNeigh(pos):
        return ((pos[0]+dx, pos[1]+dy)
                for dx, dy in move
                if pos[1]+dy > 0
                if (pos[0]+dx, pos[1]+dy) in river_depth
                if (pos[0]+dx, pos[1]+dy) not in passed)

    min_order = 1e5

    starts = sorted([e for e in river_depth if e[1] == 0],
                    key=lambda x: river_depth[x])

    for start in starts:
        # print('-' * 80)
        # print('starts', start)
        passed = {start: (None, river_depth[start], 1)}
        surround = {}
        pos = start  # last node
        length = 2   # length of steps
        for e in genNeigh(start):
            dep = max(river_depth[start], river_depth[e])
            surround[e] = (pos, dep, length, dep*1000+length)

        while surround:
            forward = sorted(surround.items(), key=lambda x: x[1][3])[0]

            if forward[1][3] >= min_order:
                break

            passed[forward[0]] = forward[1]

            # print('\n   add', forward[0], forward[1])
            # pprint(passed)
            pos = forward[0]  # last node
            length = forward[1][2] + 1  # length of steps
            for e in genNeigh(forward[0]):
                dep = max(passed[forward[0]][1], river_depth[e])
                order = dep*1000+length
                if e in surround:
                    if surround[e][3] > order:
                        surround[e] = (pos, dep, length, order)
                else:
                    surround[e] = (pos, dep, length, order)

            del surround[forward[0]]

            if forward[0][1] == len(river[0])-1:
                min_order = min(forward[1][3], min_order)
                good_path = [forward[0], passed]
                break

        # pprint(passed)

    print('summary')
    pprint(good_path)

    x = good_path[0]
    out = [x]
    while True:
        x = good_path[1][x][0]
        out.append(x)
        if x[1] == 0:
            break
    out.reverse()
    return out


river = [[2, 3, 2],
         [1, 1, 4],
         [9, 5, 2],
         [1, 4, 4],
         [1, 5, 4],
         [2, 1, 4],
         [5, 1, 2],
         [5, 5, 5],
         [8, 1, 9]]

river = [[8, 8, 8, 1, 8, 8, 1, 1, 1, 8],
         [8, 8, 8, 1, 1, 8, 1, 1, 8, 8],
         [8, 8, 1, 1, 1, 1, 8, 8, 1, 8],
         [1, 8, 1, 1, 8, 8, 1, 8, 1, 8],
         [1, 8, 8, 8, 8, 8, 1, 8, 1, 8],
         [1, 1, 1, 1, 1, 8, 8, 8, 8, 1],
         [8, 1, 1, 8, 1, 8, 8, 1, 1, 1],
         [1, 8, 8, 1, 8, 8, 8, 1, 1, 1],
         [8, 1, 8, 8, 1, 1, 1, 8, 1, 1],
         [1, 1, 1, 8, 1, 1, 8, 8, 8, 1]]

river1 = [[1, 8, 8],
          [8, 8, 8],
          [8, 8, 1],
          [8, 8, 1],
          [8, 1, 8],
          [8, 8, 1],
          [1, 1, 8],
          [8, 8, 1],
          [8, 8, 8]]

t = time.time()
pprint(shallowest_path(river))
# for _ in range(500):
#     shallowest_path(river)
print(time.time()-t)
