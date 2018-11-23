# coding: utf-8
import time
import random


def cheapest_path(t, start, finish):
    oldset = set()
    td, final, neighbordict = tdict(t)
    final[start] = [td[start], [start]]

    path = 0

    while True:
        todoset = (e for e in final.keys() if final[e] and e not in oldset)

        p = start
        m = 10000000000000
        for e in todoset:
            for neighbor in neighbordict[e]:

                if neighbor in oldset:
                    continue

                # assume setfinal[e] exists
                cost = final[e][0] + td[neighbor]
                path = final[e][1].copy()
                path.append(neighbor)

                if final[neighbor] is None:
                    # not valued yet
                    final[neighbor] = [cost, path]
                    continue

                # valued before
                if final[neighbor][0] < cost:
                    # if cheaper before, do nothing
                    continue
                # if cheaper now, update
                final[neighbor] = [cost, path]

            if final[e][0] < m:
                p = e
                m = final[e][0]

        if p == finish:
            break

        oldset.add(p)

        # if oldset == final.keys():
        #    break

    good_path = final[finish][1]
    leads = []
    for j in range(1, len(good_path)):
        diff = (good_path[j][0]-good_path[j-1][0],
                good_path[j][1]-good_path[j-1][1])
        leads.append(direct(diff))
    return leads


def direct(e):
    if e == (1, 0):
        return 'down'
    if e == (-1, 0):
        return 'up'
    if e == (0, 1):
        return 'right'
    if e == (0, -1):
        return 'left'


def get_neighbors(e):
    neighbors = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbors.append((e[0]+d[0], e[1]+d[1]))
    return neighbors


def tdict(t):
    td = dict()
    final = dict()
    neighbordict = dict()

    for j in range(len(t)):
        for k in range(len(t[0])):
            td[(j, k)] = t[j][k]
            final[(j, k)] = None

    for e in td.keys():
        neighbordict[e] = set()
        for n in get_neighbors(e):
            if n in td.keys():
                neighbordict[e].add(n)

    return td, final, neighbordict


def printfinal(final):
    for e in final.items():
        print('\t', end='')
        print(e)


t = [[1, 9, 1], [2, 9, 1], [2, 1, 1]]

begin = time.time()
print(cheapest_path(t, (0, 0), (0, 2)))
print(time.time()-begin)

tt = []
for j in range(20):
    tt.append([random.random() for e in range(20)])
begin = time.time()
print(cheapest_path(tt, (0, 0), (7, 7)))
print(time.time()-begin)

tt = []
for j in range(30):
    tt.append([random.random() for e in range(40)])
begin = time.time()
print(cheapest_path(tt, (10, 9), (19, 20)))
print(time.time()-begin)
