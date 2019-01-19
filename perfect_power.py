# code: utf-8


from math import log, floor, sqrt


def isPP(n):
    for j in range(2, floor(n)+1):
        for jj in range(2, n):
            t = j ** jj
            if t == n:
                return [j, jj]
            if t > n:
                break


print(isPP(4))
print(isPP(9))
print(isPP(125))
