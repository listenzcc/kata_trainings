# code: utf-8


def decompose(n):
    res = decom(n**2, n)
    if not sum(e**2 for e in res) == n**2:
        return None
    # print(sum(e**2 for e in res))
    return res


def decom(n2, n):
    if n2 == 0:
        return []
    if n2 == 1:
        return [1]
    if n2 == 2:
        return [1, 1]
    for j in range(int(n2 ** 0.5), 0, -1):
        if j == n:
            continue
        res = [j] + decom(n2-j**2, n)
        if check(res) and sum(e**2 for e in res) == n2:
            return sorted(res)
    return []


def check(res):
    return len(set(e for e in res)) == len(res)


print(decompose(4))
print(decompose(5))
print(decompose(8))
print(decompose(11))
print(decompose(50))
