# code: utf-8

import math


def list_squared(m, n):
    # your code
    out = []
    for k in range(m, n):
        out.append(parse(k))
        if out[-1] is None:
            out.pop()
    return out


def parse(k):
    lst = list(x for x in range(1, math.floor(k/2)+1) if k % x == 0)
    if lst == [1]:
        return None
    lst += [k]
    ss = sum(x**2 for x in lst)
    if math.sqrt(ss).is_integer():
        print(k, lst, ss)
        return [k, ss]
    return None


print(list_squared(1, 250))

parse(33)
