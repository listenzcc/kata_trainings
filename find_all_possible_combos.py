# code: utf-8

'''
Jon and Joe have received equal marks in the school examination. But, they won't reconcile in peace when equated with each other. To prove his might, Jon challenges Joe to write a program to find all possible number combos that sum to a given number. While unsure whether he would be able to accomplish this feat or not, Joe accpets the challenge. Being Joe's friend, your task is to help him out.

Task
Create a function combos, that accepts a single positive integer num (30 > num > 0) and returns an array of arrays of positive integers that sum to num.

Notes
Sub-arrays may or may not have their elements sorted.
The order of sub-arrays inside the main array does not matter.
For an optimal solution, the following operation should complete within 6000ms.
'''

import functools
import time


def combos(n):
    combos_iter(n, [])
    return res


res = []


def combos_iter(n, path):
    if n == 0:
        res.append(path)
        return
    if n == 1:
        path.append(1)
        res.append(path)
        return

    if path:
        m = min(n, path[-1])
    else:
        m = n
    for j in range(m, 0, -1):
        new_path = path.copy()
        new_path.append(j)
        combos_iter(n-j, new_path)


print(combos(2))
print(combos(3))

res = combos(5)
print('-')
for e in res:
    print(e)

t = time.time()
res16 = combos(16)
print(time.time() - t)

t = time.time()
res25 = combos(25)
print(time.time() - t)
