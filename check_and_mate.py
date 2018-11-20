# Returns an array of threats if the arrangement of
# the pieces is a check, otherwise false


def isCheck(pieces, player):
    board, king, checkarr, selfboard = parse_pieces(pieces, player)
    if player == 1:
        opp = 0
    if player == 0:
        opp = 1
    board.append(king[opp])
    xk, yk = king[player][0], king[player][1]

    for idx in range(len(pieces)):
        piece = pieces[idx]
        x, y = piece['x'], piece['y']
        p, o = piece['piece'], piece['owner']
        if o == opp:
            if p == 'rook':
                checkarr[idx] = expand(x, y, 1, 0, board, xk, yk) | expand(x, y, 0, 1, board, xk, yk) | expand(
                    x, y, -1, 0, board, xk, yk) | expand(x, y, 0, -1, board, xk, yk)
            if p == 'bishop':
                checkarr[idx] = expand(x, y, 1, 1, board, xk, yk) | expand(
                    x, y, -1, -1, board, xk, yk) | expand(x, y, -1, 1, board, xk, yk) | expand(x, y, 1, -1, board, xk, yk)
            if p == 'knight':
                checkarr[idx] = ((x+2, y+1) == (xk, yk)) | ((x-2, y-1) == (xk, yk)) | ((x+2, y-1) == (xk, yk)) | ((x-2, y+1) == (
                    xk, yk)) | ((x+1, y+2) == (xk, yk)) | ((x-1, y-2) == (xk, yk)) | ((x-1, y+2) == (xk, yk)) | ((x+1, y-2) == (xk, yk))
            if p == 'pawn':
                if player == 0:
                    checkarr[idx] = ((x+1, y+1) == (xk, yk)
                                     ) | ((x-1, y+1) == (xk, yk))
                if player == 1:
                    checkarr[idx] = ((x+1, y-1) == (xk, yk)
                                     ) | ((x-1, y-1) == (xk, yk))
            if p == 'queen':
                checkarr[idx] = expand(x, y, 1, 0, board, xk, yk) | expand(x, y, 0, 1, board, xk, yk) | expand(x, y, -1, 0, board, xk, yk) | expand(x, y, 0, -1, board, xk, yk) | expand(
                    x, y, 1, 1, board, xk, yk) | expand(x, y, -1, -1, board, xk, yk) | expand(x, y, -1, 1, board, xk, yk) | expand(x, y, 1, -1, board, xk, yk)
            if p == 'king':
                checkarr[idx] = (abs(x-xk) == 1) & (abs(y-yk) == 1)

    out = []
    for idx in range(len(pieces)):
        if checkarr[idx]:
            out.append(pieces[idx])
    return out

    pass

# Returns true if the arrangement of the
# pieces is a check mate, otherwise false


def isMate(pieces, player):
    if isCheck(pieces, player) == False:
        return False

    board, king, checkarr, selfboard = parse_pieces(pieces, player)
    if player == 1:
        opp = 0
    if player == 0:
        opp = 1
    board.append(king[opp])
    xk_, yk_ = king[player][0], king[player][1]

    total = []
    for x_ in [-1, 0, 1]:
        for y_ in [-1, 0, 1]:
            if (x_ == 0) & (y_ == 0):
                continue
            xk = xk_ + x_
            yk = yk_ + y_
            if (xk, yk) in selfboard:
                continue
            if (xk < 0) | (xk > 7) | (yk < 0) | (yk > 7):
                continue

            thismove = True
            print((xk, yk))
            for idx in range(len(pieces)):
                piece = pieces[idx]
                x, y = piece['x'], piece['y']
                if (xk, yk) == (x, y):
                    continue
                p, o = piece['piece'], piece['owner']
                if o == opp:
                    cc = False
                    print(p)
                    if p == 'rook':
                        cc = expand(x, y, 1, 0, board, xk, yk) | expand(x, y, 0, 1, board, xk, yk) | expand(
                            x, y, -1, 0, board, xk, yk) | expand(x, y, 0, -1, board, xk, yk)
                    if p == 'bishop':
                        cc = expand(x, y, 1, 1, board, xk, yk) | expand(x, y, -1, -1, board, xk, yk) | expand(
                            x, y, -1, 1, board, xk, yk) | expand(x, y, 1, -1, board, xk, yk)
                    if p == 'knight':
                        cc = ((x+2, y+1) == (xk, yk)) | ((x-2, y-1) == (xk, yk)) | ((x+2, y-1) == (xk, yk)) | ((x-2, y+1) == (xk, yk)) | (
                            (x+1, y+2) == (xk, yk)) | ((x-1, y-2) == (xk, yk)) | ((x-1, y+2) == (xk, yk)) | ((x+1, y-2) == (xk, yk))
                    if p == 'pawn':
                        if player == 0:
                            cc = ((x+1, y+1) == (xk, yk)
                                  ) | ((x-1, y+1) == (xk, yk))
                        if player == 1:
                            cc = ((x+1, y-1) == (xk, yk)
                                  ) | ((x-1, y-1) == (xk, yk))
                    if p == 'queen':
                        print((x, y))
                        print((xk, yk))
                        cc = expand(x, y, 1, 0, board, xk, yk) | expand(x, y, 0, 1, board, xk, yk) | expand(x, y, -1, 0, board, xk, yk) | expand(x, y, 0, -1, board, xk, yk) | expand(
                            x, y, 1, 1, board, xk, yk) | expand(x, y, -1, -1, board, xk, yk) | expand(x, y, -1, 1, board, xk, yk) | expand(x, y, 1, -1, board, xk, yk)
                    if p == 'king':
                        cc = (abs(x-xk) == 1) & (abs(y-yk) == 1)
                    print(cc)
                    if cc:
                        thismove = False
            total.append(thismove)

    print(total)
    if total == []:
        return True
    for t in total:
        if t:
            return False
    return True
    pass


def parse_pieces(pieces, player):
    board = []
    selfboard = []
    king = [0, 0]
    checkarr = []
    for piece in pieces:
        checkarr.append(False)
        x, y = piece['x'], piece['y']
        p, o = piece['piece'], piece['owner']
        if p == 'king':
            king[o] = (x, y)
            continue
        board.append((x, y))
        if o == player:
            selfboard.append((x, y))
    return board, king, checkarr, selfboard


def expand(x, y, dx, dy, board, xk, yk):
    # rook
    if (dx == 0) & (dy > 0):
        while y <= 7:
            y += 1
            if (x, y) == (xk, yk):
                return True
            if (x, y) in board:
                return False
        return False
    if (dx == 0) & (dy < 0):
        while y >= 0:
            y -= 1
            if (x, y) == (xk, yk):
                return True
            if (x, y) in board:
                return False
        return False
    if (dy == 0) & (dx > 0):
        while x <= 7:
            x += 1
            if (x, y) in board:
                return False
            if (x, y) == (xk, yk):
                return True
        return False
    if (dy == 0) & (dx < 0):
        while x >= 0:
            x -= 1
            if (x, y) == (xk, yk):
                return True
            if (x, y) in board:
                return False
        return False

    # bishop
    while (x >= 0) & (x <= 7) & (y >= 0) & (y <= 7):
        x += dx
        y += dy
        if (x, y) == (xk, yk):
            return True
        if (x, y) in board:
            return False
    return False


pieces = [
    {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
    {'piece': "pawn", 'owner': 0, 'x': 4, 'y': 6},
    {'piece': "pawn", 'owner': 0, 'x': 5, 'y': 6},
    {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
    {'piece': "bishop", 'owner': 0, 'x': 5, 'y': 7},
    {'piece': "bishop", 'owner': 1, 'x': 1, 'y': 4},
    {'piece': "rook", 'owner': 1, 'x': 2, 'y': 7, 'prevX': 2, 'prevY': 5}
]

print(isCheck(pieces, 0))

pieces = [
    {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
    {'piece': "rook", 'owner': 1, 'x': 3, 'y': 6},
    {'piece': "queen", 'owner': 1, 'x': 3, 'y': 7},
    {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
    {'piece': "pawn", 'owner': 0, 'x': 4, 'y': 6},
    {'piece': "pawn", 'owner': 0, 'x': 5, 'y': 6},
    {'piece': "rook", 'owner': 0, 'x': 5, 'y': 7}
]

print(isCheck(pieces, 0))
print(isMate(pieces, 0))
