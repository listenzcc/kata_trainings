def validateBattlefield(field):
    # write your magic here
    xsize = len(field)
    ysize = len(field[0])

    s = 0
    for j in range(xsize):
        for k in range(ysize):
            s += field[j][k]
    if s != (4+3+3+2+2+2+1+1+1+1):
        return False

    for j in range(xsize-1):
        for k in range(ysize-1):
            ss = field[j][k] + field[j][k+1] + field[j+1][k] + field[j+1][k+1]
            if ss > 2:
                return False
            if (field[j][k] == 1) & (field[j+1][k+1] == 1):
                return False
            if (field[j][k+1] == 1) & (field[j+1][k] == 1):
                return False

    return True

