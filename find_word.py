
board = [
    ["E", "A", "R", "A"],
    ["N", "L", "E", "C"],
    ["I", "A", "I", "S"],
    ["B", "Y", "O", "R"]
]

word = 'EACS'


def find_word(board, word):
    grid = [l+[''] for l in board] + [[''] * (len(board[0]) + 1)]

    def rc(x, y, i):
        print(grid)
        print((x, y))
        if i == len(word):
            return True
        if grid[x][y] != word[i]:
            return False
        grid[x][y] = ''
        r = any(rc(x + u, y + v, i + 1)
                for u in range(-1, 2)
                for v in range(-1, 2))
        grid[x][y] = word[i]
        print(r)
        return r
    return any(rc(x, y, 0)
               for x in range(len(board))
               for y in range(len(board[x])))


find_word(board, word)

P = {(i, j): e for j, r in enumerate(board) for i, e in enumerate(r)}

chains, word = [[p] for p in P if P[p] == word[0]], word[1:]

grid = [l+[''] for l in board] + [[''] * (len(board[0]) + 1)]
