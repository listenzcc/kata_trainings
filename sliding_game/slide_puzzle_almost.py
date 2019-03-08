# code: utf-8
from copy import deepcopy


class SlidePuzzle():
    def __init__(self, puzzle):
        self.origin = deepcopy(puzzle)
        self.puzzle = deepcopy(puzzle)
        self.size = (len(puzzle), len(puzzle[0]))
        self.mk_ground_truth()
        self.p = self.find(0)
        self.path = []
        self.path.append(deepcopy(self.puzzle))

    def solve(self):
        self.pnt()
        p = self.check()

        while self.check(self.block):
            p = self.check(self.block)
            self.position_v1(p)

        for j in range(self.size[0]-2):
            self.position_v1((j, self.size[1]-2))
            self.position_v2((j, self.size[1]-1))

        for j in range(self.size[1]-2):
            self.position_v1((self.size[0]-2, j))
            self.position_v3((self.size[0]-1, j))

        self.goto((self.size[0]-1, self.size[1]-1))

        while self.check([]):
            self.up()
            self.left()
            self.down()
            self.right()

        return self.path

    def position_v3(self, dp):
        print('working:', dp, self.gt[dp])
        if not self.p[1] == self.size[1]-1:
            self.right()
        if self.get(dp) == self.gt[dp]:
            return
        cp = self.find(self.gt[dp])

        # move cp to bottom, blank stops at cp's top
        if cp[0] == self.p[0]:
            if cp[0] == self.size[0]-1:
                self.up()
            else:
                self.down()
        self.goto((self.p[0], cp[1]))
        if not cp[0] == self.size[0]-1:
            self.up()
        cp = self.find(self.gt[dp])

        # move cp left two 2nd column
        while cp[1] > dp[1]+1:
            self.left()
            self.down()
            self.right()
            self.up()
            self.left()
            cp = self.find(self.gt[dp])

        self.right()
        self.down()
        self.left()
        self.up()
        self.left()
        self.down()
        self.right()
        self.up()
        self.left()
        self.down()
        self.right()
        self.right()
        self.up()
        self.left()
        self.left()
        self.down()
        self.right()

    def position_v2(self, dp):
        print('working:', dp, self.gt[dp])
        self.down()
        if self.get(dp) == self.gt[dp]:
            return
        cp = self.find(self.gt[dp])

        # move cp to right end, blank stops at cp's left
        if not self.size[1] - cp[1] in [1, 2]:
            if cp[0] == self.size[0]-1:
                self.goto((cp[0]-1, cp[1]))
                self.down()
            else:
                self.goto((cp[0]+1, cp[1]))
            while cp[1] < dp[1]:
                self.right()
                self.up()
                self.left()
                cp = self.find(self.gt[dp])
                if cp[1] == dp[1]:
                    break
                self.down()
                self.right()

        # blank stops at cp's left
        if cp[1] == self.p[1]:
            if cp[1] == self.size[1]-1:
                self.left()
            else:
                self.right()
        self.goto((cp[0], self.p[1]))
        if cp[1] == self.size[1]-2:
            self.left()
        cp = self.find(self.gt[dp])

        # move cp up to 2nd row
        while cp[0] > dp[0]+1:
            self.up()
            self.right()
            self.down()
            self.left()
            self.up()
            cp = self.find(self.gt[dp])

        self.down()
        self.right()
        self.up()
        self.up()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()
        self.up()
        self.up()
        self.right()
        self.down()

    def position_v1(self, dp):
        print('working:', dp, self.gt[dp])
        if self.get(dp) == self.gt[dp]:
            return
        cp = self.find(self.gt[dp])

        # move blank to cp's down
        if cp[1] == self.p[1]:
            self.goto(cp)
        else:
            if cp[0] == self.size[0]-1:
                self.goto((cp[0]-1, cp[1]))
                self.down()
            else:
                self.goto((cp[0]+1, cp[1]))
        cp = self.find(self.gt[dp])

        # fit column, blank stops at cp's down
        # right
        while cp[1] < dp[1]:
            self.right()
            self.up()
            self.left()
            self.down()
            self.right()
            cp = self.find(self.gt[dp])
            # if cp[1] == dp[1]:
            #    break
        # left
        while cp[1] > dp[1]:
            self.left()
            self.up()
            self.right()
            self.down()
            self.left()
            cp = self.find(self.gt[dp])
            # if cp[1] == dp[1]:
            #    break

        self.right()
        self.up()

        # fit row
        # down
        while cp[0] < dp[0]:
            self.down()
            self.left()
            self.up()
            if cp[0] == dp[0]:
                break
            self.right()
            self.down()
            cp = self.find(self.gt[dp])
        # up
        while cp[0] > dp[0]:
            self.up()
            self.left()
            self.down()
            if cp[0] == dp[0]:
                break
            self.right()
            self.up()
            cp = self.find(self.gt[dp])

    def mk_ground_truth(self):
        self.gt = dict()
        self.block = set()
        x = 1
        for j in range(self.size[0]):
            for k in range(self.size[1]):
                self.gt[(j, k)] = x
                x += 1
                if k > self.size[1]-3 or j > self.size[0]-3:
                    self.block.add((j, k))
        self.gt[(j, k)] = 0

    def check(self, block=[]):
        for p in self.gt.keys():
            if p in block:
                continue
            if not self.get(p) == self.gt[p]:
                return p
        return 0

    def get(self, p):
        assert((p[0], p[1]) in self.gt.keys())
        return self.puzzle[p[0]][p[1]]

    def set(self, p, x):
        assert((p[0], p[1]) in self.gt.keys())
        self.puzzle[p[0]][p[1]] = x

    def find(self, x):
        for p in self.gt.keys():
            if self.get(p) == x:
                return p

    def pnt(self):
        print('-'*60)
        for j, p in enumerate(self.puzzle):
            print('%d:' % j, ' '.join('%2d' % e for e in p))

    def goto(self, d):
        while self.p[0] < d[0]:
            self.down()
        while self.p[1] < d[1]:
            self.right()
        while self.p[1] > d[1]:
            self.left()
        while self.p[0] > d[0]:
            self.up()

    def step(self, dr):
        p_ = (self.p[0]+dr[0], self.p[1]+dr[1])
        self.set(self.p, self.get(p_))
        self.set(p_, 0)
        self.p = p_
        self.pnt()
        self.path.append(deepcopy(self.puzzle))
        print(self.path)

    def left(self):
        self.step((0, -1))

    def right(self):
        self.step((0, 1))

    def up(self):
        self.step((-1, 0))

    def down(self):
        self.step((1, 0))


puzzle1 = [
    [4, 1, 3],
    [2, 8, 0],
    [7, 6, 5]
]
puzzle11 = [[8, 2, 1], [3, 7, 0], [4, 6, 5]]
puzzle2 = [
    [10, 3, 6, 4],
    [1, 5, 8, 0],
    [2, 13, 7, 15],
    [14, 9, 12, 11]
]
puzzle3 = [
    [3, 7, 14, 15, 10],
    [1, 0, 5, 9, 4],
    [16, 2, 11, 12, 8],
    [17, 6, 13, 18, 20],
    [21, 22, 23, 19, 24]
]
board = [
    [4, 1, 2],
    [5, 0, 3]
]
simpleExample = [
    [1, 2, 3, 4],
    [5, 0, 6, 8],
    [9, 10, 7, 11],
    [13, 14, 15, 12]
]

sp = SlidePuzzle(puzzle11)
sp.solve()
