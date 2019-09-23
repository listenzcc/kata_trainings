# coding: utf-8

import time
from pprint import pprint
print(__doc__)

repeat = 1000
size = 10

raw_board = {(j, k): j*k for j in range(size) for k in range(size)}
# pprint(board)

_moves = [(-2, 1), (-2, -1), (-1, -2), (1, -2),
          (2, -1), (2, 1), (1, 2), (-1, 2)]

board = raw_board.copy()

_allow = {e: 0 for e in board if board[e] % 2}


def genNeighs(pos):
    return [(pos[0]+dx, pos[1]+dy)
            for dx, dy in _moves
            if (pos[0]+dx, pos[1]+dy) in _allow]


_neighs = {pos: genNeighs(pos) for pos in board}

board = raw_board.copy()
t = time.time()
for r in range(repeat):
    for pos in board:
        for e in genNeighs(pos):
            board[e] += 1
print(time.time() - t)


board = raw_board.copy()
t = time.time()
for r in range(repeat):
    for pos in board:
        subs = [e for e in _neighs[pos] if e in _allow]
        for e in subs:
            board[e] += 1
print(time.time() - t)
