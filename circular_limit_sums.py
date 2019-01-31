import numpy as np
MOD = 12345787


def mpow(a, n, p):
    if n == 0:
        return np.eye(a.shape[0])
    if n == 1:
        return a % p
    if n > 1:
        b = mpow(a, n // 2, p)
        b = np.dot(b, b) % p
        if n % 2 == 0:
            return b
        else:
            return np.dot(a, b) % p


def insane_cls(n, m):
    s = 0
    for g in range(m + 1):
        init = np.zeros((m + 1, 1), dtype=np.int)
        init[(g, 0)] = 1
        A = np.ones((m + 1, m + 1), dtype=np.int)
        for j in range(1, m + 1):
            A[j][m+1-j:] = 0
        print(g, end=' ')
        print('-'*60)
        print(init)
        print(A)
        print(mpow(A, n-1, MOD))
        print(np.dot(mpow(A, n-1, MOD), init))
        print(np.dot(mpow(A, n-1, MOD), init)[:(m-g+1)])
        s += np.sum(np.dot(mpow(A, n - 1, MOD), init)[:(m - g + 1)])
    return s % MOD


print(insane_cls(5, 2))
