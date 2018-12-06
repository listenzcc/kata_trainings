# coding: utf-8
import time


def tower(base, h, m):
    """Return base ** base ** ... ** base, where the height is h, modulo m. """
    if m == 1:
        return 0
    if base == 1:
        return 1
    if h == 0:
        return 1
    if h == 1:
        return base % m

    G, t = totient(m)

    if base in G:
        f = base
        for j in range(h-2):
            f = (base ** f) % t
        return (base ** f) % m

    return 100

    pass


def totient(m):
    G = set()
    G.add(1)
    d = set()
    for j in range(2, m):
        if j in d:
            continue
        if m % j == 0:
            d.add(j)
            jj = j
            while jj < m:
                jj += j
                d.add(jj)
            continue
        G.add(j)
    return G, len(G)


t0 = time.time()
G, t = totient(65519)
print(t)
print(time.time()-t0)

print(tower(2, 5, 65519))

print(tower(3, 9, 4))

print(tower(7, 7, 9))

print(tower(7, 4, 8))
