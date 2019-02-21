# code:utf-8


def blox_solver(ar):
    pnt(ar)
    mymap, BX = parse(ar)
    print(mymap)
    print(BX)

    old_step = set()
    path = {'': BX['B']}
    print(path)

    print(get_possible(BX['B'], mymap, BX))

    for j in range(10000):
        # print('%d: ' % j, path, '\n\t', old_step, '\n')
        x = update(path, old_step, mymap, BX)
        if x:
            return x

    pass


def update(path, old_step, mymap, BX):
    short_path = sorted(path.keys(), key=lambda d: len(d))[0]
    possible = get_possible(path[short_path], mymap, BX)
    for p in possible.items():
        if str(p[1]) in old_step:
            continue
        path[short_path+p[0]] = p[1]
        if p[1] == BX['X']:
            return short_path+p[0]
    old_step.add(str(path[short_path]))
    path.pop(short_path)
    return False


def get_possible(coor, mymap, BX):
    possible = {}

    if len(coor) == 1:
        row, col = coor[0]
        if mymap.get((row-1, col), 0) and mymap.get((row-2, col), 0):
            possible['U'] = [(row-1, col), (row-2, col)]
        if mymap.get((row+1, col), 0) and mymap.get((row+2, col), 0):
            possible['D'] = [(row+1, col), (row+2, col)]
        if mymap.get((row, col-1), 0) and mymap.get((row, col-2), 0):
            possible['L'] = [(row, col-1), (row, col-2)]
        if mymap.get((row, col+1), 0) and mymap.get((row, col+2), 0):
            possible['R'] = [(row, col+1), (row, col+2)]
        return possible

    if len(coor) == 2 and coor[0][0] == coor[1][0]:
        row = coor[0][0]
        cols = (coor[0][1], coor[1][1])
        if mymap.get((row-1, cols[0]), 0) and mymap.get((row-1, cols[1]), 0):
            possible['U'] = [(row-1, cols[0]), (row-1, cols[1])]
        if mymap.get((row+1, cols[0]), 0) and mymap.get((row+1, cols[1]), 0):
            possible['D'] = [(row+1, cols[0]), (row+1, cols[1])]
        if mymap.get((row, min(cols)-1), 0) or [(row, min(cols)-1)] == BX['X']:
            possible['L'] = [(row, min(cols)-1)]
        if mymap.get((row, max(cols)+1), 0) or [(row, max(cols)+1)] == BX['X']:
            possible['R'] = [(row, max(cols)+1)]

    if len(coor) == 2 and coor[0][1] == coor[1][1]:
        col = coor[0][1]
        rows = (coor[0][0], coor[1][0])
        if mymap.get((min(rows)-1, col), 0) or [(min(rows)-1, col)] == BX['X']:
            possible['U'] = [(min(rows)-1, col)]
        if mymap.get((max(rows)+1, col), 0) or [(max(rows)+1, col)] == BX['X']:
            possible['D'] = [(max(rows)+1, col)]
        if mymap.get((rows[0], col-1), 0) and mymap.get((rows[1], col-1), 0):
            possible['L'] = [(rows[0], col-1), (rows[1], col-1)]
        if mymap.get((rows[0], col+1), 0) and mymap.get((rows[1], col+1), 0):
            possible['R'] = [(rows[0], col+1), (rows[1], col+1)]

    return possible


def pnt(ar):
    print('-' * 60)
    print('\n'.join(ar))


def parse(ar):
    mymap = dict()
    BX = {'B': [], 'X': []}
    for r, row in enumerate(ar):
        for c, col in enumerate(row):
            if col in ['1', 'B', 'X']:
                mymap[(r, c)] = 1
            if col == 'X':
                BX['X'].append((r, c))
            if col == 'B':
                BX['B'].append((r, c))
    return mymap, BX


example_tests = [
    ['1110000000',
     '1111110000',
     '1111111B10',
     '0111111B11',
     '0000011X11',
     '0000001110'],
    ['1110000000',
     '1B11110000',
     '1111111110',
     '0111111111',
     '0000011X11',
     '0000001110'],
    ['000000111111100',
     '111100111001100',
     '111111111001111',
     '1B11000000011X1',
     '111100000001111',
     '000000000000111'],
    ['00011111110000',
     '00011111110000',
     '11110000011100',
     '11100000001100',
     '11100000001100',
     '1B100111111111',
     '11100111111111',
     '000001X1001111',
     '00000111001111'],
    ['11111100000',
     '1B111100000',
     '11110111100',
     '11100111110',
     '10000001111',
     '11110000111',
     '11110000111',
     '00110111111',
     '01111111111',
     '0110011X100',
     '01100011100'],
    ['000001111110000',
     '000001001110000',
     '000001001111100',
     'B11111000001111',
     '0000111000011X1',
     '000011100000111',
     '000000100110000',
     '000000111110000',
     '000000111110000',
     '000000011100000']
]


blox_solver(example_tests[1])
blox_solver(example_tests[2])
