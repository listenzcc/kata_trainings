#! code: utf-8


class TextClass():
    def __init__(self):
        self.name = 'text instance'

    def describe(self, string):
        self.describe = string

    def it(self, string):
        self.it = string

    def assert_equals(self, a, b):
        if a == b:
            pass
        else:
            print('Wrong:\n %s\n %s' % (a, b))


def mk_dict(string):
    d = {}
    for c in string:
        if c >= 'a' and c <= 'z':
            if d.get(c, None) is None:
                d[c] = 1
            else:
                d[c] += 1
    return d


def merge(d1, d2):
    d = {}
    for e in d1.keys():
        if d1[e] == 1:
            continue
        d[e] = (d1[e], '1:')

    for e in d2.keys():
        if d2[e] == 1:
            continue
        if e in d.keys():
            if d[e][0] == d2[e]:
                d[e] = (d2[e], '=:')
            if d[e][0] < d2[e]:
                d[e] = (d2[e], '2:')
        else:
            d[e] = (d2[e], '2:')

    return d


def parse_d(d):
    outs = {}
    for e in d.keys():
        if d[e][0] in outs.keys():
            outs[d[e][0]].append(d[e][1]+e*d[e][0])
        else:
            outs[d[e][0]] = [d[e][1]+e*d[e][0]]

    for e in outs.keys():
        outs[e] = sorted(outs[e])
    lists = sorted(outs.items(), reverse=True, key=lambda e: e[0])

    out_string = '/'.join(['/'.join(e[1]) for e in lists])

    return out_string


def mix(s1, s2):
    print('-' * 80)
    print(s1)
    print(s2)
    d1 = mk_dict(s1)
    # print(d1)
    d2 = mk_dict(s2)
    # print(d2)

    d = merge(d1, d2)
    print(d)

    o = parse_d(d)
    print(o)

    return o


Test = TextClass()

Test.describe("Mix")
Test.it("Basic Tests")
Test.assert_equals(mix("Are they here", "yes, they are here"),
                   "2:eeeee/2:yy/=:hh/=:rr")
Test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"),
                   "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
Test.assert_equals(mix(" In many languages", " there's a pair of functions"),
                   "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
Test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
Test.assert_equals(mix("codewars", "codewars"), "")
Test.assert_equals(mix("A generation must confront the looming ",
                       "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
