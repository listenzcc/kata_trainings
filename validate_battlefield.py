# code: utf-8

import itertools


def validate_battlefield(battleField):
    s = sum(battleField[j][k] for j in range(10) for k in range(10))
    if not s == 1*4 + 2*3 + 3*2 + 4*1:
        return False

    cc = dict()
    for n in [4, 3, 2]:
        cc[n] = []
        for j in range(10):
            for k in range(10):
                if k+n <= 10:
                    if list(battleField[j][k+x] for x in range(n)) == list(1 for x in range(n)):
                        cc[n].append(set((j, k+x) for x in range(n)))
                if j+n <= 10:
                    if list(battleField[j+x][k] for x in range(n)) == list(1 for x in range(n)):
                        cc[n].append(set((j+x, k) for x in range(n)))
    for c in cc.items():
        print(c)
    if len(cc[4]) < 1:
        return False
    if len(cc[3]) < 2:
        return False
    if len(cc[2]) < 3:
        return False

    for c4 in itertools.combinations(cc[4], 1):
        for c3 in itertools.combinations(cc[3], 2):
            ss = c4[0].union(c3[0]).union(c3[1])
            if not len(ss) == 1*4 + 2*3:
                continue
            for c2 in itertools.combinations(cc[2], 3):
                ss = c4[0].union(c3[0]).union(c3[1]).union(
                    c2[0]).union(c2[1]).union(c2[2])
                if len(ss) == 1*4 + 2*3 + 3*2:
                    print(ss)
                    return True

    return False


bf = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

bf = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

bf = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
      [0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
      [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

bf = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
      [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
      [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
      [0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

validate_battlefield(bf)
