def expand(expr):
    print(expr)
    a = []
    b = []
    c = []
    num1 = False
    num2 = False
    num3 = False
    firstsign = False
    for e in expr:
        if e == '(':
            num1 = True
            firstsign = True
            num2 = False
            num3 = False
            continue
        if firstsign:
            a.append(e)
            firstsign = False
            continue
        if e in ['+', '-']:
            num1 = False
            num2 = True
            b.append(e)
            num3 = False
            continue
        if e == ')':
            num1 = False
            num2 = False
            num3 = True
            continue
        if num1:
            a.append(e)
            continue
        if num2:
            b.append(e)
            continue
        if num3:
            c.append(e)
            continue
    raw = []
    x = a.pop()
    if not(a):
        a = ['1']
    if a == ['-']:
        a.append('1')
    c.pop(0)
    a = int(''.join(a))
    b = int(''.join(b))
    c = int(''.join(c))

    if c == 0:
        return '1'
    for c2 in range(c+1):
        c1 = c - c2
        f0 = nchoosek(c, c2)
        f1 = a ** c1
        f2 = b ** c2
        raw.append(f0*f1*f2)

    out = ''
    for c2 in range(c+1):
        c1 = c - c2
        tmp = raw.pop(0)
        if tmp > 0:
            out += '+'
        if c1 == 0:
            out += str(tmp)
            continue
        if tmp == -1:
            out += '-'
        if tmp == 1:
            out += ''
        if abs(tmp) != 1:
            out += str(tmp)
        if c1 > 0:
            if c1 > 1:
                out += '%s^%d' % (x, c1)
            if c1 == 1:
                out += x

    if out[0] == '+':
        out = out[1::]

    return out
    pass


def nchoosek(n, k):
    a = rank(n)
    b = rank(k)
    c = rank(n-k)
    return int(a/(b*c))


def rank(n):
    o = 1
    for e in range(n):
        o *= (e+1)
    return o


expand("(x+1)^0")
expand("(x+1)^1")
expand("(x+1)^2")

expand("(x-1)^0")
expand("(x-1)^1")
expand("(x-1)^2")

expand("(5m+3)^4")
expand("(2x-3)^3")
expand("(7x-7)^0")

expand("(-5m+3)^4")
expand("(-2k-3)^3")
expand("(-7x-7)^0")
