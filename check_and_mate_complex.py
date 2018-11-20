# Returns an array of threats if the arrangement of
# the pieces is a check, otherwise false


def isCheck(pieces, player):
    pieces_arr, king = get_pieces_arr(pieces, player)
    xk, yk, pk, ok = parse(king)
    n = len(pieces)
    out = []
    for j in range(n):
        piece = pieces[j]
        x, y, p, o = parse(piece)
        if o == player:
            continue
        if p == 'king':
            possible = possible_king(piece, pieces_arr)
        if p == 'rook':
            possible = possible_rook(piece, pieces_arr)
        if p == 'bishop':
            possible = possible_bishop(piece, pieces_arr)
        if p == 'queen':
            possible = possible_queen(piece, pieces_arr)
        if p == 'pawn':
            possible = possible_pawn(piece, pieces_arr)
        if p == 'knight':
            possible = possible_knight(piece, pieces_arr)
        if (xk, yk) in possible:
            out.append(piece)
    return out

    pass

# Returns true if the arrangement of the
# pieces is a check mate, otherwise false


def isMate(pieces, player):
    print(player)
    for e in pieces:
        print(e)
    print('------------')
    if not(isCheck(pieces, player)):
        return False

    pieces_arr, king = get_pieces_arr(pieces, player)
    xk, yk, pk, ok = parse(king)
    n = len(pieces)
    for j in range(n):
        piece = pieces[j]
        x, y, p, o = parse(piece)
        if o != player:
            continue
        if p == 'king':
            possible = possible_king(piece, pieces_arr)
        if p == 'rook':
            possible = possible_rook(piece, pieces_arr)
        if p == 'bishop':
            possible = possible_bishop(piece, pieces_arr)
        if p == 'queen':
            possible = possible_queen(piece, pieces_arr)
        if p == 'pawn':
            possible = possible_pawn(piece, pieces_arr)
        if p == 'knight':
            possible = possible_knight(piece, pieces_arr)

        print(piece)
        print(possible)

        for po in possible:
            newpieces = list(e.copy() for e in pieces)
            newpieces[j]['x'] = po[0]
            newpieces[j]['y'] = po[1]
            dead = pieces_arr[idx_xy(po[0], po[1])]
            if (p == 'pawn') & (po[0] != x):
                if not(dead):
                    dead = pieces_arr[idx_xy(po[0], y)]
            print(po, end='\t')
            print('xxxxx\t', end='')
            print(dead)
            if dead:
                newpieces.pop(pieces.index(dead))
            if not(isCheck(newpieces, player)):
                print('eacspe!!!!!!!')
                return False

    return True

    pass


def possible_knight(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    for d in [(1, 2), (-1, 2), (1, -2), (-1, -2),
              (2, 1), (-2, 1), (2, -1), (-2, -1)]:
        x_, y_ = x+d[0], y+d[1]
        if not(in_board(x_, y_)):
            continue
        if not(pieces_arr[idx_xy(x_, y_)]):
            possible.append((x_, y_))
            continue
        if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
            possible.append((x_, y_))
            continue
    return possible


def possible_pawn(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    if o == 1:
        a = 1
        s = 1
    if o == 0:
        a = -1
        s = 6
    x_, y_1 = x, y+a
    if in_board(x_, y_1):
        if not(pieces_arr[idx_xy(x_, y_1)]):
            possible.append((x_, y_1))
    if y == s:
        x_, y_2 = x, y+a+a
        if in_board(x_, y_2):
            if not(pieces_arr[idx_xy(x_, y_1)]):
                if not(pieces_arr[idx_xy(x_, y_2)]):
                    possible.append((x_, y_2))
    for j in [-1, 1]:
        x_, y_ = x+j, y+a
        if not(in_board(x_, y_)):
            continue
        if pieces_arr[idx_xy(x_, y_)]:
            if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
                possible.append((x_, y_))

    for j in [-1, 1]:
        x_, y_ = x+j, y
        if not(in_board(x_, y_+a)):
            continue
        if not(pieces_arr[idx_xy(x_, y_)]):
            continue
        if pieces_arr[idx_xy(x_, y_)]['owner'] == o:
            continue
        if pieces_arr[idx_xy(x_, y_)]['piece'] == 'pawn':
            possible.append((x_, y_+a))

    return possible


def possible_king(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    for j in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if (j == 0) & (k == 0):
                continue
            x_, y_ = x+j, y+k
            if not(in_board(x_, y_)):
                continue
            if not(pieces_arr[idx_xy(x_, y_)]):
                possible.append((x_, y_))
                continue
            if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
                possible.append((x_, y_))
                continue
    return possible


def possible_rook(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x_, y_ = x, y
        while True:
            x_ += d[0]
            y_ += d[1]
            if not(in_board(x_, y_)):
                break
            if not(pieces_arr[idx_xy(x_, y_)]):
                possible.append((x_, y_))
                continue
            if pieces_arr[idx_xy(x_, y_)]['owner'] == o:
                break
            if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
                possible.append((x_, y_))
                break
    return possible


def possible_bishop(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    for d in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        x_, y_ = x, y
        while True:
            x_ += d[0]
            y_ += d[1]
            if not(in_board(x_, y_)):
                break
            if not(pieces_arr[idx_xy(x_, y_)]):
                possible.append((x_, y_))
                continue
            if pieces_arr[idx_xy(x_, y_)]['owner'] == o:
                break
            if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
                possible.append((x_, y_))
                break
    return possible


def possible_queen(piece, pieces_arr):
    possible = []
    x, y, p, o = parse(piece)
    for d in [(1, 1), (-1, 1), (1, -1), (-1, -1),
              (1, 0), (0, 1), (-1, 0), (0, -1)]:
        x_, y_ = x, y
        while True:
            x_ += d[0]
            y_ += d[1]
            if not(in_board(x_, y_)):
                break
            if not(pieces_arr[idx_xy(x_, y_)]):
                possible.append((x_, y_))
                continue
            if pieces_arr[idx_xy(x_, y_)]['owner'] == o:
                break
            if pieces_arr[idx_xy(x_, y_)]['owner'] != o:
                possible.append((x_, y_))
                break
    return possible


def in_board(x, y):
    legal = list(range(8))
    return (x in legal) & (y in legal)


def idx_xy(x, y):
    return x*10 + y


def xy_idx(idx):
    x = int(idx/10)
    y = idx % 10
    return x, y


def parse(piece):
    return piece['x'], piece['y'], piece['piece'], piece['owner']


def get_pieces_arr(pieces, player):
    arr = list(None for j in range(100))
    for piece in pieces:
        x, y, p, o = parse(piece)
        if (p == 'king') & (o == player):
            king = piece
        arr[idx_xy(x, y)] = piece

    return arr, king


pieces = [
    {'piece': 'king', 'y': 3, 'x': 5, 'owner': 1},
    {'piece': 'pawn', 'prevX': 4, 'y': 4, 'x': 4, 'owner': 0, 'prevY': 6},
    {'piece': 'pawn', 'y': 6, 'x': 5, 'owner': 0},
    {'piece': 'king', 'y': 7, 'x': 4, 'owner': 0},
    {'piece': 'knight', 'y': 5, 'x': 2, 'owner': 0},
    {'piece': 'pawn', 'y': 4, 'x': 3, 'owner': 1},
    {'piece': 'knight', 'y': 3, 'x': 3, 'owner': 1},
    {'piece': 'pawn', 'y': 3, 'x': 4, 'owner': 1},
    {'piece': 'bishop', 'y': 2, 'x': 4, 'owner': 1},
    {'piece': 'rook', 'y': 2, 'x': 5, 'owner': 1},
    {'piece': 'queen', 'y': 5, 'x': 6, 'owner': 0},
]

player = 1
isMate(pieces, player)
