# code: utf-8
import time


class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solution = []
        self.parse_puzzle()

    def solve(self):

        def solve_iter(fix_dict, possible_dict):
            # print state for each iter, largely slowdown the function
            # print(self.pnt(fix_dict))

            # return True if all fixed
            if len(fix_dict) == 81:
                # get solution
                self.solution.append(self.pnt(fix_dict))
                # assert finish
                assert(self.finish_check())
                return False

            # sort possibles as uncertainty
            sorted_possible = sorted(
                possible_dict.items(), key=lambda d: len(d[1]))
            if len(sorted_possible[0][1]) == 0:
                return False

            # choose least uncertain as (j, k)
            least_uncertain = sorted_possible[0]
            j, k = least_uncertain[0]

            # collect 20 neighbors
            neighbor_set = set(self.fix_dict.get(xy, 0)
                               for xy in self.neighbor_nodes[(j, k)])

            # for each candidate in least uncertainties
            for candidate in least_uncertain[1]:
                # not choose if conflict with existing neighbors
                if candidate in neighbor_set:
                    continue
                # make new_fix_dict, new_possible_dict
                new_possible_dict = possible_dict.copy()
                new_fix_dict = fix_dict.copy()
                # de-uncertainty of (j, k)
                new_possible_dict.pop((j, k))
                # update neighbors if they are uncertain
                for neighbor in self.neighbor_nodes[(j, k)]:
                    if candidate in new_possible_dict.get(neighbor, []):
                        new_possible_dict[neighbor] = new_possible_dict[
                            neighbor] - {candidate}
                        # stop update if possibles is empty
                        # since it will stop in next iter anyway
                        if len(new_possible_dict[neighbor]) == 0:
                            break
                # add (j, k) as candidate in new_fix_dict
                new_fix_dict[(j, k)] = candidate
                # go, go, go
                if solve_iter(new_fix_dict, new_possible_dict):
                    return True
            # all candidates failed
            return False

        # start iter
        solve_iter(self.fix_dict, self.possible_dict)

        assert(not self.solution == [])
        if len(self.solution) > 1:
            print('multi solution.')
            return self.solution

        return self.solution

    def finish_check(self):
        # check if finish
        # for each 27 blocks
        for block in self.block_27:
            all_set = set(self.solution[-1][e[0]][e[1]] for e in block)
            # return False, if not 1, 2, ..., 8, 9
            if not all_set == set(range(1, 10)):
                return False
        # return True, if all checked
        return True

    def pnt(self, fix_dict):
        # print and return board
        # init
        board = [['=' for _ in range(9)] for __ in range(9)]
        # for all fix nodes, set as number
        for it in fix_dict.items():
            board[it[0][0]][it[0][1]] = it[1]
        # print
        print('-' * 60)
        for j, b in enumerate(board):
            print('%02d:' % (j*9), ' '.join(str(e) for e in b))
        # return board
        return board

    def parse_puzzle(self):
        # protect code
        assert(len(self.puzzle) == 9)
        assert(len(self.puzzle[0]) == 9)
        # init rules
        self.mk_rules()
        # fix nodes as input
        self.fix_dict = dict()
        # uncertain nodes as input
        self.possible_dict = dict()
        for j, k in self.all_nodes:
            # protect code
            assert(self.puzzle[j][k] in range(10))
            # uncertain
            if self.puzzle[j][k] == 0:
                tmp = set(range(1, 10))
                for neighbor in self.neighbor_nodes[(j, k)]:
                    tmp -= {self.puzzle[neighbor[0]][neighbor[1]]}
                assert(len(tmp) > 0)
                if len(tmp) > 1:
                    self.possible_dict[(j, k)] = tmp
                else:
                    # if only one possible
                    self.fix_dict[(j, k)] = tmp.pop()
            # fix
            else:
                self.fix_dict[(j, k)] = self.puzzle[j][k]

    def mk_rules(self):
        # there are 27 9-nodes blocks
        self.block_27 = []
        for j in range(9):
            self.block_27.append(set((j, y) for y in range(9)))
        for k in range(9):
            self.block_27.append(set((x, k) for x in range(9)))
        for j in [0, 3, 6]:
            for k in [0, 3, 6]:
                self.block_27.append(set((j+x, k+y)
                                         for x in range(3) for y in range(3)))

        # table 20 neighbors for each node
        self.neighbor_nodes = dict()
        # all 81 nodes
        self.all_nodes = []
        for j in range(9):
            for k in range(9):
                # add a node
                self.all_nodes.append((j, k))
                # add neighbors
                tmp = set()
                tmp = tmp.union(set((x, k) for x in range(9)))
                tmp = tmp.union(set((j, y) for y in range(9)))
                tmp = tmp.union(set((j//3*3+x, k//3*3+y)
                                    for x in range(3) for y in range(3)))
                tmp -= {(j, k)}
                self.neighbor_nodes[(j, k)] = tmp


def solve(puzzle):
    sudoku = Sudoku(puzzle)
    return sudoku.solve()


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

ppp = [puzzle1, puzzle2, puzzle3, puzzle4]
t = time.time()
for pp in ppp:
    solution = solve(pp)
    print(solution)
    print(len(solution))
print(time.time() - t)
