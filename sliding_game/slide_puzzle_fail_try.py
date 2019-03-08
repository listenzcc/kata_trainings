# code: utf-8
from copy import deepcopy


def slide_puzzle(puzzle):
    print('-'*60)
    for j, p in enumerate(puzzle):
        print('%d:' % j, p)

    lp = mk_legal_positions(puzzle)

    past = dict()

    def go_iter(puzzle, last=None):
        if last is not None:
            past[parse_puzzle(puzzle, lp)] = parse_puzzle(last, lp)
        print(puzzle, back_idx(puzzle, lp))
        if check_finish(puzzle, lp):
            print(puzzle)
            return True
        # past.add(parse_puzzle(puzzle, lp))
        return any(go_iter(e, puzzle) for e in possible_state(puzzle, lp) if parse_puzzle(e, lp) not in past.keys())

    go_iter(puzzle)

    final = deepcopy(puzzle)
    for e in lp.items():
        final[e[0][0]][e[0][1]] = e[1]
    x = parse_puzzle(final, lp)
    while x in past.keys():
        print(x)
        x = past[x]

    pass


def back_idx(puzzle, lp):
    pp = [e for e in parse_puzzle(puzzle, lp)]
    pp.remove(0)
    bi = 0
    for j in range(len(pp)):
        bi += sum(pp[j] > e for e in pp[j+1:])
    return bi


def find_0(puzzle):
    for j in range(len(puzzle)):
        for k in range(len(puzzle[0])):
            if puzzle[j][k] == 0:
                return (j, k)
    pass


def possible_move(puzzle, lp):
    j, k = find_0(puzzle)
    return (j, k), [e for e in
                    [(j-1, k), (j+1, k), (j, k-1), (j, k+1)]
                    if e in lp.keys()]


def possible_state(puzzle, lp):
    p, move = possible_move(puzzle, lp)
    return sorted([switch(puzzle, p, m) for m in move], key=lambda d: back_idx(d, lp))


def switch(puzzle, a, b):
    puzzle = deepcopy(puzzle)
    puzzle[a[0]][a[1]] = puzzle[b[0]][b[1]]
    puzzle[b[0]][b[1]] = 0
    return puzzle


def check_finish(puzzle, lp):
    return all(lp[e] == puzzle[e[0]][e[1]] for e in lp.keys())


def mk_legal_positions(puzzle):
    legal_positions = dict()
    x = 1
    for j in range(len(puzzle)):
        for k in range(len(puzzle[0])):
            legal_positions[(j, k)] = x
            x += 1
    legal_positions[(j, k)] = 0
    return legal_positions


def parse_puzzle(puzzle, lp):
    return tuple(puzzle[e[0]][e[1]] for e in lp.keys())


puzzle1 = [
    [4, 1, 3],
    [2, 8, 0],
    [7, 6, 5]
]
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

slide_puzzle(board)
# slide_puzzle(puzzle1)

# slide_puzzle(simpleExample)
