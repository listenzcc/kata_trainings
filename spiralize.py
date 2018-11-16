def printspiral(spiral):
    for e in spiral:
        print(e)


def spiralize(size):
    # Make a snake
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1, 1], [0, 1]]

    spiral = []
    for j in range(size):
        tmp = list(range(size))
        for k in range(size):
            tmp[k] = 0
        spiral.append(tmp)

    spiral[0][0] = 1
    x, y = 0, 1
    dx, dy = 0, 1
    t = 0
    while True:
        t += 1
        if t > 300:
            break
        spiral[x][y] = 1
        print('%d, %d, %d, %d' % (x, y, dx, dy))
        printspiral(spiral)
        if check(spiral, x, y, dx, dy, size):
            dx, dy = turn(dx, dy)
        print('%d, %d, %d, %d' % (x, y, dx, dy))
        print('')
        if check(spiral, x, y, dx, dy, size):
            print('done')
            break
        x += dx
        y += dy
    if size % 2 == 0:
        spiral[x][y] = 0
    return spiral


def check(spiral, x, y, dx, dy, size):
    if dx < 0:
        if x == 0:
            return True
    if dx > 0:
        if x == size-1:
            return True
    if dy < 0:
        if y == 0:
            return True
    if dy > 0:
        if y == size-1:
            return True

    if spiral[x+dx][y+dy] == 1:
        return True

    if dy == 0:
        if x+2*dx < 0:
            return False
        if x+2*dx > size-1:
            return False
    if dx == 0:
        if y+2*dy < 0:
            return False
        if y+2*dy > size-1:
            return False

    if spiral[x+2*dx][y+2*dy] == 1:
        return True

    return False


def turn(dx, dy):
    if (dx, dy) == (0, 1):
        return 1, 0
    if (dx, dy) == (1, 0):
        return 0, -1
    if (dx, dy) == (0, -1):
        return -1, 0
    if (dx, dy) == (-1, 0):
        return 0, 1


s3 = spiralize(3)
s5 = spiralize(5)
s6 = spiralize(6)
s8 = spiralize(8)

print('hello')
print('a')
printspiral(s3)
printspiral(s5)
printspiral(s6)
printspiral(s8)
