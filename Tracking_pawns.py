# coding: utf-8

'''
A chess board is normally played with 16 pawns and 16 other pieces, for this kata a variant will be played with only the pawns. All other pieces will not be on the board.
For information on how pawns move, refer here

Write a function that can turn a list of pawn moves into a visual representation of the resulting board.
A chess move will be represented by a string,

"c3"
This move represents a pawn moving to c3. If it was white to move, the move would represent a pawn from c2 moving to c3. If it was black to move, a pawn would move from c4 to c3, because black moves in the other direction.
The first move in the list and every other move will be for white's pieces.

The letter represents the column, while the number represents the row of the square where the piece is moving

Captures are represented differently from normal moves:

"bxc3"
represents a pawn on the column represented by 'b' (the second column) capturing a pawn on c3.

For the sake of this kata a chess board will be represented by a list like this one:

[[".",".",".",".",".",".",".","."],
 ["p","p","p","p","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P","P","P","P","P","P"],
 [".",".",".",".",".",".",".","."]]
Here is an example of the board with the squares labeled:

[["a8","b8","c8","d8","e8","f8","g8","h8"],
 ["a7","b7","c7","d7","e7","f7","g7","h7"],
 ["a6","b6","c6","d6","e6","f6","g6","h6"],
 ["a5","b5","c5","d5","e5","f5","g5","h5"],
 ["a4","b4","c4","d4","e4","f4","g4","h4"],
 ["a3","b3","c3","d3","e3","f3","g3","h3"],
 ["a2","b2","c2","d2","e2","f2","g2","h2"],
 ["a1","b1","c1","d1","e1","f1","g1","h1"]]
White pawns are represented by capital 'P' while black pawns are lowercase 'p'.

A few examples

If the list/array of moves is: ["c3"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p","p","p","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".","P",".",".",".",".","."],
 ["P","P",".","P","P","P","P","P"],
 [".",".",".",".",".",".",".","."]]
add a few more moves,

If the list/array of moves is: ["d4", "d5", "f3", "c6", "f4"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p",".",".","p","p","p","p"],
 [".",".","p",".",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".","P",".","P",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P",".","P",".","P","P"],
 [".",".",".",".",".",".",".","."]]
now to add a capture...

If the list/array of moves is: ["d4", "d5", "f3", "c6", "f4", "c5", "dxc5"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p",".",".","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".","P","p",".",".",".","."],
 [".",".",".",".",".","P",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P",".","P",".","P","P"],
 [".",".",".",".",".",".",".","."]]
If an invalid move (a move is added that no pawn could perform, a capture where there is no piece, a move to a square where there is already a piece, etc.) is found in the list of moves, return '(move) is invalid'.

If the list/array of moves is: ["e6"]
>>>
"e6 is invalid"
If the list/array of moves is: ["e4", "d5", "exf5"]
>>>
"exf5 is invalid"
The list passed to pawn_move_tracker / PawnMoveTracker.movePawns will always be a list of strings in the form (regex pattern): [a-g][1-8] or [a-g]x[a-g][1-8].

Notes:
In the case of a capture, the first lowercase letter will always be adjacent to the second in the alphabet, a move like axc5 will never be passed.
A pawn can move two spaces on its first move
There are no cases with the 'en-passant' rule.
'''

from pprint import pprint


def raisem(m):
    return '%s is invalid' % m


def empty_board():
    return [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]


table = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
    '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
}


def pawn_move_tracker(moves):
    pawns = [
        dict(a=[2], b=[2], c=[2], d=[2], e=[2], f=[2], g=[2], h=[2]),
        dict(a=[7], b=[7], c=[7], d=[7], e=[7], f=[7], g=[7], h=[7]),
    ]

    for j, m in enumerate(moves):
        chars = ['P', 'p']
        board = empty_board()
        for flag in [0, 1]:
            for col, row in pawns[flag].items():
                for r in row:
                    board[7-table[str(r)]][table[col]] = chars[flag]
        pprint(board)

        flag = j % 2
        print(j, flag, m)

        if len(m) == 2:
            # move
            col = m[0]
            row = int(m[1])
            for f in [0, 1]:
                # return invalid if target position is not empty.
                if row in pawns[0][col]:
                    return raisem(m)
            if flag == 0:
                group = pawns[0]
                # if it is normal forward
                if row-1 in group[col]:
                    group[col].remove(row-1)
                    group[col].append(row)
                    continue
                # if it is initial forawrd
                if row == 4 and 2 in group[col]:
                    group[col].remove(2)
                    group[col].append(4)
                    continue
            else:
                group = pawns[1]
                # if it is normal forward
                if row+1 in group[col]:
                    group[col].remove(row+1)
                    group[col].append(str(row))
                    continue
                # if it is initial forawrd
                if row == 5 and 7 in group[col]:
                    group[col].remove(7)
                    group[col].append(5)
                    continue
            return raisem(m)

        if len(m) == 4:
            # capture
            col0 = m[0]
            col1 = m[2]
            row = int(m[3])
            if flag == 0:
                group = pawns[0]
                opp = pawns[1]
                # if target position is invalid
                if all([row-1 in group[col0],
                        row in opp[col1]]):
                    opp[col1].remove(row)
                    group[col0].remove(row-1)
                    group[col1].append(row)
                    continue
            else:
                group = pawns[1]
                opp = pawns[0]
                # if target position is invalid
                if all([row+1 in group[col0],
                        row in opp[col1]]):
                    opp[col1].remove(row)
                    group[col0].remove(row+1)
                    group[col1].append(row)
                    continue

            return raisem(m)

    chars = ['P', 'p']
    board = empty_board()
    for flag in [0, 1]:
        for col, row in pawns[flag].items():
            for r in row:
                board[7-table[str(r)]][table[col]] = chars[flag]
    pprint(board)
    return board


pprint(pawn_move_tracker(["e3", "d6", "e4", "a6"]))
pprint(pawn_move_tracker(["e4", "d5", "d3", "dxe4"]))
