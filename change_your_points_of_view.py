#! code: utf-8


class Point(object):
    def __init__(self, a, b):
        self.p = (a, b)

    def __call__(self):
        return self.p

    def fst(self):
        return self.p[0]

    def snd(self):
        return self.p[1]

    def sq(self, o):
        return sum((x-y)**2 for x, y in zip(self.p, o.p))

    def line(self, o):
        (a, b), (c, d) = self.p, o.p
        l, m = d-b, a-c
        return [l, m, -m*b-l*a]


def point(a, b):
    return Point(a, b)


fst = Point.fst
snd = Point.snd
sqr_dist = Point.sq
line = Point.line
