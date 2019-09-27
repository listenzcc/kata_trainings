# coding: utf-8

'''Task
You are given a chessBoard, a 2d integer array that contains only 0 or 1. 0 represents a chess piece and 1 represents a empty grid. It's always square shape.

Your task is to count the number of squares made of empty grids.

The smallest size of the square is 2 x 2. The biggest size of the square is n x n, where n is the size of chess board.

A square can overlap the part of other squares. For example:

If

chessBoard=[
  [1,1,1],
  [1,1,1],
  [1,1,1]
]
...there are four 2 x 2 squares in the chess board:

[1,1, ]  [ ,1,1]  [ , , ]  [ , , ]
[1,1, ]  [ ,1,1]  [1,1, ]  [ ,1,1]
[ , , ]  [ , , ]  [1,1, ]  [ ,1,1]
And one 3 x 3 square:

[1,1,1]
[1,1,1]
[1,1,1]
Your output should be an object/dict. Each item in it should be: size:number, where size is the square's size, and number is the number of squares.

For example, if there are four 2 x 2 squares and one 3 x 3 square in the chess board, the output should be: {2:4,3:1} (or any equivalent hash structure in your language). The order of items is not important, {3:1,2:4} is also a valid output.

If there is no square in the chess board, just return {}.

Note
2 <= chessBoard.length <= 120
5 fixed testcases

100 random testcases, testing for correctness of solution

100 random testcases, testing for performance of code

All inputs are valid.

Pay attention to code performance.

If my reference solution gives the wrong result in the random tests, please let me know(post an issue).

Example
For

chessBoard = [
  [1,1],
  [1,1]
]
the output should be {2:1}.

For

chessBoard = [
  [0,1],
  [1,1]
]
the output should be {}.

For

chessBoard = [
  [1,1,1],
  [1,1,1],
  [1,1,1]
]
the output should be {2:4,3:1}.

For

chessBoard = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
the output should be {}.'''

from collections import defaultdict
import time
from pprint import pprint

print(__doc__)


def count_slow(chessBoard):
    N = len(chessBoard)

    all_possible = {(j, k): [e for e in range(2, N-max(j, k)+1)]
                    for j in range(N-1)
                    for k in range(N-1)
                    if chessBoard[j][k] == 1}
    pprint(all_possible)

    squares = {}

    for pos, nlist in all_possible.items():
        for n in nlist:
            if any(chessBoard[pos[0]+j][pos[1]+k] == 0
                   for j in range(n) for k in range(n)):
                print(pos, n, 'fails.')
            else:
                print(pos, n, 'passes.')
                if n in squares:
                    squares[n] += 1
                else:
                    squares[n] = 1

    return squares


def count(chessBoard):
    # Initialize:
    board = chessBoard.copy()
    tally = defaultdict(int)

    # Compute Longest square ending in bottom right corner of each element and tally up:
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            # Edge detection:
            if i == 0 or j == 0:
                continue

            # Compute & Tally:
            if element:
                n = board[i][j] = min(
                    board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                for x in range(n, 1, -1):
                    tally[x] += 1

            print()
            print(i, j)
            pprint(board)

    return tally


chessBoard = [[0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [0, 1, 1, 0, 1],
              [1, 1, 1, 1, 1]]

# chessBoard = [[1, 1, 1, 1, 1],
#               [1, 1, 1, 1, 1],
#               [1, 1, 1, 1, 0],
#               [1, 1, 0, 1, 0],
#               [1, 1, 0, 0, 1]]

print(count(chessBoard))
