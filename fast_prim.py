# coding: utf-8
import time


def prim(m):
    all_num = list(range(m))
    prim = set()

    prim.add(1)
    all_num[1] = 0

    for j in range(1, m):
        if all_num[j] == 0:
            continue
        t = all_num[j]
        t_ = t
        prim.add(t)
        while t < m:
            all_num[t] = 0
            t += t_

    return prim


t = time.time()
print(prim(99))
print(time.time()-t)
