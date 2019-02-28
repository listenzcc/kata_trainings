# code: utf-8

from copy import deepcopy
import time


def sudoku(puzzle):
    puzzle_dict = parse(puzzle)
    # for e in puzzle_dict.items():
    #     print(e[0], ':', e[1])
    results = guess(puzzle_dict)
    solution = puzzle.copy()
    for it in results.items():
        solution[it[0][0]][it[0][1]] = it[1].pop()
    return solution


def guess(puzzle_dict):
    # pnt(puzzle_dict)

    for it in puzzle_dict.items():
        if len(it[1]) == 0:
            return False

    if check(puzzle_dict):
        # print(puzzle_dict)
        return puzzle_dict

    sort_uncertain = sorted(puzzle_dict.items(), key=lambda d: len(d[1]))
    if len(sort_uncertain[-1][1]) == 1:
        return False

    for min_uncertain in sort_uncertain:
        if len(min_uncertain[1]) > 1:
            break

    j, k = min_uncertain[0]
    jj, kk = j//3*3, k//3*3
    for c in min_uncertain[1]:
        force_continue = False
        new_puzzle_dict = puzzle_dict.copy()

        for x in range(9):
            if c in new_puzzle_dict[(x, k)]:
                new_puzzle_dict[(x, k)] = puzzle_dict[(x, k)].copy() - {c}
                if len(new_puzzle_dict[(x, k)]) == 0:
                    force_continue = True
                    break
        if force_continue:
            continue

        for y in range(9):
            if c in new_puzzle_dict[(j, y)]:
                new_puzzle_dict[(j, y)] = puzzle_dict[(j, y)].copy() - {c}
                if len(new_puzzle_dict[(j, y)]) == 0:
                    force_continue = True
                    break
        if force_continue:
            continue

        for x in range(3):
            for y in range(3):
                if c in new_puzzle_dict[(jj+x, kk+y)]:
                    new_puzzle_dict[(jj+x, kk+y)
                                    ] = puzzle_dict[(jj+x, kk+y)].copy() - {c}
                    if len(new_puzzle_dict[(jj+x, kk+y)]) == 0:
                        force_continue = True
                        break
        if force_continue:
            continue

        new_puzzle_dict[(j, k)] = {c}
        # print(j, k, jj, kk, c, new_puzzle_dict)
        x = guess(new_puzzle_dict)
        if not x:
            continue
        return x


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


def ij2kl(ij):
    """Transform (row, col) to (square, tail). The inverse transformation
    is the same (just like magic!!!).
    """
    i, j = ij
    k = i // 3 * 3 + j // 3
    l = i % 3 * 3 + j % 3
    return k, l


class SudokuBoard(object):

    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append([0]*9)
        self.row_col = {}  # Set of possible numbers in the tile (row,col)
        self.unsure = set()  # Unsure tiles (those with more than one possible numbers)
        for i in range(9):
            for j in range(9):
                self.row_col[(i, j)] = set(range(1, 10))
                self.unsure.add((i, j))
        self.row_num = {}  # Set of possible column indices for (row, num)
        for i in range(9):
            for num in range(1, 10):
                self.row_num[(i, num)] = set(range(9))
        # Set of possible row indices for (col, num)
        self.col_num = deepcopy(self.row_num)
        # Set of possible tail indices for (square, num)
        self.square_num = deepcopy(self.row_num)
        self.to_put = set()  # Import queue keeping all confirmed putting moves (row, col, num)

    def add_to_put(self, triplet):
        """Add a triplet (row, col, num) to the queue `self.to_put`."""
        if not triplet in self.to_put:
            self.to_put.add(triplet)

    def remove_and_infer(self, row, col, num):
        """Remove the possibility to put `(row,col,num)` on the board.
        Update info for inferring. When there is only one possibility left,
        add it to the queue `self.to_put`.
        """
        square, tail = ij2kl((row, col))
        numset = self.row_col[(row, col)]
        if num in numset:
            numset.remove(num)
            if len(numset) == 1:
                for n in numset:
                    self.add_to_put((row, col, n))
        rowset = self.col_num[(col, num)]
        if row in rowset:
            rowset.remove(row)
            if len(rowset) == 1:
                for r in rowset:
                    self.add_to_put((r, col, num))
        colset = self.row_num[(row, num)]
        if col in colset:
            colset.remove(col)
            if len(colset) == 1:
                for c in colset:
                    self.add_to_put((row, c, num))
        tailset = self.square_num[(square, num)]
        if tail in tailset:
            tailset.remove(tail)
            if len(tailset) == 1:
                for t in tailset:
                    i, j = ij2kl((square, t))
                    self.add_to_put((i, j, num))

    def put(self):
        """Put all numbers in the queue `self.to_put` on the board.
        Remove impossible cases by calling `self.remove_and_infer`.
        """
        while self.to_put:
            row, col, num = self.to_put.pop()
            square, tail = ij2kl((row, col))
            if not (num in self.row_col[(row, col)] and
                    row in self.col_num[(col, num)] and
                    col in self.row_num[(row, num)] and
                    tail in self.square_num[(square, num)]):
                return False
            else:
                self.row_col[(row, col)] = {num}
                self.col_num[(col, num)] = {row}
                self.row_num[(row, num)] = {col}
                self.square_num[(square, num)] = {tail}
                for r in range(9):
                    if r != row:
                        self.remove_and_infer(r, col, num)
                for c in range(9):
                    if c != col:
                        self.remove_and_infer(row, c, num)
                for t in range(9):
                    if t != tail:
                        i, j = ij2kl((square, t))
                        self.remove_and_infer(i, j, num)
                for n in range(1, 10):
                    if n != num:
                        self.remove_and_infer(row, col, n)
                self.board[row][col] = num
                self.unsure.remove((row, col))
        return True

    def solve(self):
        if not self.put():
            return None
        if not self.unsure:
            return self.board
        else:
            unsure_list = sorted(
                list(self.unsure), key=lambda x: len(self.row_col[x]))
            # Choose the tile with fewest possibilities
            row, col = unsure_list[0]
            while len(self.row_col[(row, col)]) > 1:
                num = self.row_col[(row, col)].pop()
                self.row_col[(row, col)].add(num)
                new_self = deepcopy(self)
                new_self.add_to_put((row, col, num))
                board = new_self.solve()
                if board:
                    return board
                else:
                    self.remove_and_infer(row, col, num)
            # now len(self.row_col[(row,col)]) == 1 and `self.to_put` is not empty
            if self.put():
                return self.solve()
            else:
                return None


def solve_fast(board):
    haha = SudokuBoard()
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num > 0:
                haha.add_to_put((i, j, num))
    res = haha.solve()
    return res


def sudoku_fast(puzzle):
    block_27, block_list = mk_block()
    puzzle_list = mk_list(puzzle)
    results = []

    def is_check(puzzle_list):
        # -2, means failed
        # -1, means good
        # j, means guess in j
        if [] in puzzle_list:
            return -2
        lens = sorted(set(len(e) for e in puzzle_list))
        if lens == [1]:
            for idx_9 in block_27:
                # if not sorted(puzzle_list[e][0] for e in idx_9) == list(range(1, 10)):
                if not len(set(puzzle_list[e][0] for e in idx_9)) == 9:
                    return -2
            return -1
        for j, e in enumerate(puzzle_list):
            if len(e) == lens[1]:
                return j

    def solve_iter(puzzle_list):
        # pnt_list(puzzle_list)
        idx = is_check(puzzle_list)
        if idx == -2:
            return False
        if idx == -1:
            pnt_list(puzzle_list)
            results.append(puzzle_list)
            return True
        # print(idx, puzzle_list[idx])
        for c in puzzle_list[idx]:
            new_puzzle_list = puzzle_list.copy()
            for neighbor_idx in block_list[idx]:
                if c in puzzle_list[neighbor_idx]:
                    new_puzzle_list[neighbor_idx] = [
                        e for e in puzzle_list[neighbor_idx] if not e == c]
                    if new_puzzle_list[neighbor_idx] == []:
                        break
            new_puzzle_list[idx] = [c]
            if solve_iter(new_puzzle_list):
                return True
        return 0

    solve_iter(puzzle_list)

    solution = puzzle.copy()
    for j in range(9):
        for k in range(9):
            solution[j][k] = results[0][sub2idx(j, k)][0]
    return solution


def pnt_list(puzzle_list):
    board = [[0 for _ in range(9)] for __ in range(9)]
    for j in range(9):
        for k in range(9):
            idx = sub2idx(j, k)
            if len(puzzle_list[idx]) == 1:
                board[j][k] = '%d' % puzzle_list[idx][0]
            if len(puzzle_list[idx]) == 0:
                board[j][k] = 'x'
            if len(puzzle_list[idx]) > 1:
                board[j][k] = '='
    print('-' * 60)
    for j, b in enumerate(board):
        print('%2d:' % (j*9), ' '.join(e for e in b))


def sub2idx(j, k):
    return j*9 + k


def mk_block():
    block_27 = []
    for j in range(9):
        block_27.append(set(sub2idx(j, y) for y in range(9)))
    for k in range(9):
        block_27.append(set(sub2idx(x, k) for x in range(9)))
    for j in [0, 3, 6]:
        for k in [0, 3, 6]:
            block_27.append(set(sub2idx(j+x, k+y)
                                for x in range(3) for y in range(3)))
    block_list = []
    for j in range(9):
        for k in range(9):
            tmp = set()
            tmp = tmp.union(set(sub2idx(x, k) for x in range(9)))
            tmp = tmp.union(set(sub2idx(j, y) for y in range(9)))
            tmp = tmp.union(set(sub2idx(j//3*3+x, k//3*3+y)
                                for x in range(3) for y in range(3)))
            block_list.append(tmp)
    return block_27, block_list


def mk_list(puzzle):
    puzzle_list = []
    for j in range(9):
        for k in range(9):
            if puzzle[j][k] == 0:
                all = set(range(1, 10))
                sub1 = set(puzzle[x][k] for x in range(9))
                sub2 = set(puzzle[j][y] for y in range(9))
                sub3 = set(puzzle[j//3*3+x][k//3*3+y]
                           for x in range(3) for y in range(3))
                possible = all - sub1 - sub2 - sub3
                puzzle_list.append([e for e in possible])
            else:
                puzzle_list.append([puzzle[j][k]])
    return puzzle_list


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

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


pp = [puzzle1, puzzle2, puzzle3, puzzle4] + \
    [puzzle1, puzzle2, puzzle3, puzzle4]

t = time.time()
for j in range(4):
    print(solve_fast(pp.pop()))
print(time.time() - t)

t = time.time()
for j in range(4):
    print(sudoku_fast(pp.pop()))
print(time.time() - t)

# t = time.time()
# print(sudoku(pp.pop()))
# print(time.time() - t)
