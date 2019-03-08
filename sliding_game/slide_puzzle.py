# code: utf-8
from copy import deepcopy


class SlidePuzzle():
    def __init__(self, puzzle):
        self.origin = deepcopy(puzzle)
        self.puzzle = deepcopy(puzzle)
        self.sz = (len(puzzle), len(puzzle[0]))
        self.mk_ground_truth()
        self.p = self.find(0)
        self.pnt()
        self.path = []

    def solve(self):
        # for p in [(0, 0), (0, 1), (0, 2), (0, 3)]:
        p = self.check()
        while p:
            if p[0] > self.sz[0]-3:
                break
            if p[1] == self.sz[1]-1:
                self.move(self.gt[p], (p[0]+1, p[1]))
                self.move_v2(p[0])
            else:
                self.move(self.gt[p], p)
            p = self.check()

        for p in [(self.sz[0]-2, j) for j in range(self.sz[1]-2)]:
            print('_:', p)
            self.move(self.gt[p], p)
            self.goto((self.sz[0]-1, self.sz[1]-1))
            if self.gt[(p[0]+1, p[1])] == self.get((p[0]+1, p[1])):
                continue
            self.move(self.gt[(p[0]+1, p[1])], (p[0], p[1]+1))
            self.move_v3(p[1])

        self.goto((self.sz[0]-1, self.sz[1]-1))

        for j in range(4):
            self.up()
            self.left()
            self.down()
            self.right()
            if not self.check():
                print('done.')
                return self.path

        for j in range(4):
            self.left()
            self.up()
            self.right()
            self.down()
            if not self.check():
                print('done.')
                return self.path

        return

    def move_v3(self, c):
        print('settling:_',
              self.get((self.sz[0]-2, 0)), self.get((self.sz[0]-2, 1)))

        # move blank to x's down
        self.goto((self.sz[0]-1, c+1))

        # fit last 2 rows
        self.up()
        self.right()
        self.down()
        self.left()
        self.left()
        self.up()
        self.right()
        self.down()
        self.right()
        self.up()
        self.left()
        self.left()
        self.down()
        self.right()

    def move_v2(self, r):
        print('settling:',
              self.get((r, self.sz[1]-2)), self.get((r+1, self.sz[1]-1)))
        if self.p[0] == r:
            self.down()
            return

        # move blank to x's down
        self.goto((r+2, self.sz[1]-1))

        # fit last 2 columns
        self.up()
        self.left()
        self.up()
        self.right()
        self.down()
        self.left()
        self.up()
        self.right()
        self.down()
        self.down()
        self.left()
        self.up()
        self.up()
        self.right()
        self.down()

    def move(self, x, dest):
        print('moving:', x, dest)
        if self.get(dest) == x:
            return

        # goto x as init
        self.goto(self.find(x))

        # make sure blank at x's down
        cp = self.find(x)
        if not cp[0] == self.p[0]-1:
            if cp[0] == self.p[0]+1:
                self.down()
            else:
                if cp[0] == self.sz[0]-1:
                    self.up()
                    self.goto((cp[0]-1, cp[1]))
                    self.down()
                else:
                    self.down()
                    self.goto((cp[0]+1, cp[1]))

        # fit column, blank stops at x's down
        cp = self.find(x)
        # right
        while cp[1] < dest[1]:
            self.right()
            self.up()
            self.left()
            self.down()
            self.right()
            cp = self.find(x)
        # left
        while cp[1] > dest[1]:
            self.left()
            self.up()
            self.right()
            self.down()
            self.left()
            cp = self.find(x)

        # fit row
        cp = self.find(x)
        if cp[1] == self.sz[1]-1:
            self.left()
            self.up()
            while cp[0] > dest[0]:
                self.up()
                self.right()
                self.down()
                self.left()
                self.up()
                cp = self.find(x)
        else:
            self.right()
            self.up()
            while cp[0] > dest[0]:
                self.up()
                self.left()
                self.down()
                self.right()
                self.up()
                cp = self.find(x)

    def mk_ground_truth(self):
        self.gt = dict()
        x = 1
        for j in range(self.sz[0]):
            for k in range(self.sz[1]):
                self.gt[(j, k)] = x
                x += 1
        self.gt[(j, k)] = 0

    def check(self):
        for p in self.gt.keys():
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
        self.path.append(self.get(p_))
        self.set(self.p, self.get(p_))
        self.set(p_, 0)
        self.p = p_
        self.pnt()

    def left(self):
        self.step((0, -1))

    def right(self):
        self.step((0, 1))

    def up(self):
        self.step((-1, 0))

    def down(self):
        self.step((1, 0))


puzzle3 = [
    [4, 1, 3],
    [2, 8, 0],
    [7, 6, 5]
]
puzzle31 = [
    [8, 2, 1],
    [3, 7, 0],
    [4, 6, 5]
]
puzzle4 = [
    [10, 3, 6, 4],
    [1, 5, 8, 0],
    [2, 13, 7, 15],
    [14, 9, 12, 11]
]
puzzle41 = [[2, 0, 11, 6], [1, 15, 5, 4], [13, 10, 3, 12], [14, 9, 7, 8]]
puzzle5 = [
    [3, 7, 14, 15, 10],
    [1, 0, 5, 9, 4],
    [16, 2, 11, 12, 8],
    [17, 6, 13, 18, 20],
    [21, 22, 23, 19, 24]
]

simpleExample = [
    [1, 2, 3, 4],
    [5, 0, 6, 8],
    [9, 10, 7, 11],
    [13, 14, 15, 12]
]

sp = SlidePuzzle(puzzle41)
s = sp.solve()
