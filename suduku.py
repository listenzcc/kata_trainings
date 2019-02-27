# code: utf-8

from copy import deepcopy
import time


def sudoku(puzzle):
    puzzle_dict = parse(puzzle)
    # for e in puzzle_dict.items():
    #     print(e[0], ':', e[1])
    results = []
    guess(puzzle_dict, results)
    solution = puzzle.copy()
    for it in results[0].items():
        solution[it[0][0]][it[0][1]] = it[1].pop()
    return solution


def guess(puzzle_dict, results, pos=None, c=None):
    # pnt(puzzle_dict)

    for it in puzzle_dict.items():
        if len(it[1]) == 0:
            return False

    if check(puzzle_dict):
        results.append(puzzle_dict)
        print(puzzle_dict)
        return True

    sort_uncertain = sorted(puzzle_dict.items(), key=lambda d: len(d[1]))
    if len(sort_uncertain[-1][1]) == 1:
        return False

    for min_uncertain in sort_uncertain:
        if len(min_uncertain[1]) > 1:
            break

    j, k = min_uncertain[0]
    jj, kk = j//3*3, k//3*3
    for c in min_uncertain[1]:
        new_puzzle_dict = puzzle_dict.copy()
        for it in puzzle_dict.items():
            new_puzzle_dict[it[0]] = it[1].copy()
        for x in range(9):
            new_puzzle_dict[(x, k)] = puzzle_dict[(x, k)].copy() - {c}
        for y in range(9):
            new_puzzle_dict[(j, y)] = puzzle_dict[(j, y)].copy() - {c}
        for x in range(3):
            for y in range(3):
                new_puzzle_dict[(jj+x, kk+y)
                                ] = puzzle_dict[(jj+x, kk+y)].copy() - {c}
        new_puzzle_dict[(j, k)] = {c}
        # print(j, k, jj, kk, c, new_puzzle_dict)
        if guess(new_puzzle_dict, results):
            return True


def pnt(puzzle_dict):
    puzzle = [['-' for _ in range(9)] for __ in range(9)]
    for it in puzzle_dict.items():
        if len(it[1]) == 0:
            puzzle[it[0][0]][it[0][1]] = 'x'
            continue
        if len(it[1]) == 1:
            puzzle[it[0][0]][it[0][1]] = '%d' % it[1].copy().pop()
            continue
        puzzle[it[0][0]][it[0][1]] = '='
    print('-'*60)
    for e in puzzle:
        print(' '.join(e))


def check(puzzle_dict):
    puzzle_dict = puzzle_dict.copy()
    for it in puzzle_dict.items():
        if not len(it[1]) == 1:
            return False
        puzzle_dict[it[0]] = it[1].copy().pop()
    for j in range(9):
        for k in range(9):
            if not len(set(puzzle_dict[(x, k)] for x in range(9))) == 9:
                return False
            if not len(set(puzzle_dict[(j, y)] for y in range(9))) == 9:
                return False
            if not len(set(puzzle_dict[(j//3*3+x, k//3*3+y)] for x in range(3) for y in range(3))) == 9:
                return False
    return True


def parse(puzzle):
    puzzle_dict = dict()
    for j in range(9):
        for k in range(9):
            if puzzle[j][k] == 0:
                all = set(range(1, 10))
                sub1 = set(puzzle[x][k] for x in range(9))
                sub2 = set(puzzle[j][y] for y in range(9))
                sub3 = set(puzzle[j//3*3+x][k//3*3+y]
                           for x in range(3) for y in range(3))
                possible = all - sub1 - sub2 - sub3
                puzzle_dict[(j, k)] = possible
            else:
                puzzle_dict[(j, k)] = {puzzle[j][k]}
    return puzzle_dict


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle = [[9, 0, 6, 0, 7, 0, 4, 0, 3], [0, 0, 0, 4, 0, 0, 2, 0, 0], [0, 7, 0, 0, 2, 3, 0, 1, 0], [5, 0, 0, 0, 0, 0, 1, 0, 0], [
    0, 4, 0, 2, 0, 8, 0, 6, 0], [0, 0, 3, 0, 0, 0, 0, 0, 5], [0, 3, 0, 7, 0, 0, 0, 5, 0], [0, 0, 7, 0, 0, 5, 0, 0, 0], [4, 0, 5, 0, 1, 0, 7, 0, 8]]

puzzle = [[0, 8, 0, 0, 0, 9, 7, 4, 3], [0, 5, 0, 0, 0, 8, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 5, 0, 0, 0], [
    0, 0, 0, 8, 0, 4, 0, 0, 0], [0, 0, 0, 3, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 7, 0], [0, 3, 0, 5, 0, 0, 0, 8, 0], [9, 7, 2, 4, 0, 0, 0, 5, 0]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

t = time.time()
puzzle_dict = sudoku(puzzle)
print(time.time() - t)
print(puzzle_dict)
