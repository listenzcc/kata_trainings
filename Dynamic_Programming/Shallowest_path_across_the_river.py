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
                if (pos[0]+dx, pos[1]+dy) not in dp_map)

    min_depth = [1e5]

    def travel(start):
        for _ in range(1000):
            edge = dict()
            for pos, value in dp_map.items():
                for neigh in genNeigh(pos):
                    depth_neigh = max(value[1], river_depth[neigh])
                    idx = depth_neigh*1000 + dp_map[pos][2]*100 - neigh[1]
                    if neigh in edge:
                        if edge[neigh][2] > idx:
                            edge[neigh] = [pos, depth_neigh, idx]
                        else:
                            pass
                    else:
                        edge[neigh] = [pos, depth_neigh, idx]

            shallow = sorted((
                # 0 order
                edge[neigh][2],
                # 1 depth of neigh
                edge[neigh][1],
                # 2 postion of edge
                neigh,
                # 3 position of pos
                edge[neigh][0])
                for neigh in edge)

            shallow = shallow[0]

            dp_map[shallow[2]] = (shallow[3], shallow[1],
                                  dp_map[shallow[3]][2]+1)

            # Too deep yet
            if shallow[1] > min_depth[0]:
                break

            # Reach right
            if shallow[2][1] == len(river[0]) - 1:
                min_depth[0] = shallow[1]
                path.append((dp_map, min_depth[0]))
                break

    path = []
    for j in range(len(river)):
        start = (j, 0)
        if not start == (4, 0):
            continue
        dp_map = {start: (None, river_depth[start], 1)}
        travel(start)

    shallow_path = [e[0] for e in path if e[1] == min_depth[0]]

    min_length = 1000000
    for e in shallow_path:
        pos = [x for x in e if x[1] == len(river[0])-1][0]
        pp = [pos]
        while True:
            pos = e[pos][0]
            pp.append(pos)
            if pos[1] == 0:
                break
        pp.reverse()
        if len(pp) < min_length:
            min_pp = pp
            min_length = len(pp)

    return min_pp


river = [[8, 8, 8, 8],
         [8, 8, 8, 8],
         [8, 8, 8, 8],
         [1, 1, 1, 8],
         [1, 8, 1, 8],
         [1, 8, 1, 8],
         [1, 8, 1, 8],
         [8, 8, 1, 8],
         [8, 8, 1, 1]]

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

rive = [[2, 3, 2],
        [1, 1, 4],
        [9, 5, 2],
        [1, 4, 4],
        [1, 5, 4],
        [2, 1, 4],
        [5, 1, 2],
        [5, 5, 5],
        [8, 1, 9]]

pprint(shallowest_path(river))
