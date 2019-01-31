import numpy as np
import itertools as it

import operator
from functools import reduce
from math import factorial as fact


def c(n, k):
    if n == 0:
        return 1
    return fact(n) // (fact(k) * fact(n-k))


def cm(n, k, m):
    return (c(n//m, k//m) * c(n % m, k % m)) % m


def tri_bicolor_tiling_0(n, r, g, b):
    # Your Code Here
    print(n, r, g, b)
    o = count(n, r, g)
    o += count(n, r, b)
    o += count(n, g, b)
    return o % 12345787


def count(n, x, y):
    o = 0
    m = 12345787
    for j in range(1, 10000000):
        if x*j >= n:
            break
        for k in range(1, 1000000000):
            if x*j + y*k > n:
                break
            nn = n
            nn -= (x-1)*j
            nn -= (y-1)*k
            o += cm(nn, j, m) * cm(nn-j, k, m)
            o %= m
    return o


def insane_tri_bicolor_tiling(n, r, g, b):
    print(n, r, g, b)
    print('-'*60)
    n_max_3_colors = sum(insane_multicolor_tiling(n, lengths)
                         for lengths in ((1, r, g), (1, r, b), (1, g, b)))
    print('-'*60)
    n_max_2_colors = sum(insane_multicolor_tiling(n, lengths)
                         for lengths in ((1, r), (1, g), (1, b)))
    return (n_max_3_colors + (-2)*n_max_2_colors + 3)  # .number


def insane_multicolor_tiling(n, lengths):
    max_length = max(lengths)
    m = np.asmatrix(np.zeros((max_length + 1, max_length + 1), dtype=Modular))
    for i in lengths:
        m[0, i - 1] += 1
    for i in range(1, max_length + 1):
        m[i, i - 1] = 1  # Modular(1)
    print(m)
    out = (m ** n)
    print(out)
    return out[0, 0]


class Modular:
    def __init__(self, number=0):
        self.number = number % 12345787

    def __add__(self, other):
        return (Modular(self.number + other.number) if isinstance(other, Modular) else
                Modular(self.number + other) if isinstance(other, int) else NotImplemented)

    def __radd__(self, other):
        return self.__add__(other) if isinstance(other, int) else NotImplemented

    def __mul__(self, other):
        return (Modular(self.number * other.number) if isinstance(other, Modular) else
                Modular(self.number * other) if isinstance(other, int) else NotImplemented)

    def __rmul__(self, other):
        return self.__mul__(other) if isinstance(other, int) else NotImplemented


print(insane_tri_bicolor_tiling(100, 2, 3, 4))
