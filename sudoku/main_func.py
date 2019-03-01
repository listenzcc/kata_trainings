# code: utf-8

from copy import deepcopy
from sudoku_simple import sudoku as sudoku_simple
from sudoku import sudoku as sudoku_slow
from sudoku import solve_fast as sudoku_fastest
from sudoku import sudoku_fast as sudoku_faster
import time

puzzle1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle2 = [[9, 0, 6, 0, 7, 0, 4, 0, 3],
           [0, 0, 0, 4, 0, 0, 2, 0, 0],
           [0, 7, 0, 0, 2, 3, 0, 1, 0],
           [5, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 4, 0, 2, 0, 8, 0, 6, 0],
           [0, 0, 3, 0, 0, 0, 0, 0, 5],
           [0, 3, 0, 7, 0, 0, 0, 5, 0],
           [0, 0, 7, 0, 0, 5, 0, 0, 0],
           [4, 0, 5, 0, 1, 0, 7, 0, 8]]

puzzle3 = [[0, 8, 0, 0, 0, 9, 7, 4, 3],
           [0, 5, 0, 0, 0, 8, 0, 1, 0],
           [0, 1, 0, 0, 0, 0, 0, 0, 0],
           [8, 0, 0, 0, 0, 5, 0, 0, 0],
           [0, 0, 0, 8, 0, 4, 0, 0, 0],
           [0, 0, 0, 3, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 7, 0],
           [0, 3, 0, 5, 0, 0, 0, 8, 0],
           [9, 7, 2, 4, 0, 0, 0, 5, 0]]

puzzle4 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 3, 6, 0, 0, 0, 0, 0],
           [0, 7, 0, 0, 9, 0, 2, 0, 0],
           [0, 5, 0, 0, 0, 7, 0, 0, 0],
           [0, 0, 0, 0, 4, 5, 7, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 3, 0],
           [0, 0, 1, 0, 0, 0, 0, 6, 8],
           [0, 0, 8, 5, 0, 0, 0, 1, 0],
           [0, 9, 0, 0, 0, 0, 4, 0, 0]]


pp = [puzzle1, puzzle2, puzzle3, puzzle4]
t = time.time()
while pp:
    print(sudoku_simple(deepcopy(pp.pop())))
print(time.time() - t)

pp = [puzzle1, puzzle2, puzzle3, puzzle4]
t = time.time()
while pp:
    print(sudoku_slow(deepcopy(pp.pop())))
print(time.time() - t)

pp = [puzzle1, puzzle2, puzzle3, puzzle4]
t = time.time()
while pp:
    print(sudoku_fastest(deepcopy(pp.pop())))
print(time.time() - t)

pp = [puzzle1, puzzle2, puzzle3, puzzle4]
t = time.time()
while pp:
    print(sudoku_faster(deepcopy(pp.pop())))
print(time.time() - t)
