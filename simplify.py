# code: utf-8

import numpy as np


def cal_bmi(b, m):
    mi = np.linalg.inv(m)
    bmi = np.matmul(b, mi)
    return bmi


M = np.array([
    [2, -1, 0, 0],
    [0, 1, -1, -1],
    [1, 1, 0, -1],
])

print('-'*60)
b = np.array([1, 1, 1])
m = M[:, [0, 1, 2]]
bmi = cal_bmi(b, m)
print(np.matmul(bmi, M))

print('-'*60)
b = np.array([1, 1, 0])
m = M[:, [0, 1, 3]]
bmi = cal_bmi(b, m)
print(np.matmul(bmi, M))

print('-'*60)
b = np.array([1, 1, 0])
m = M[:, [0, 2, 3]]
bmi = cal_bmi(b, m)
print(np.matmul(bmi, M))

print('-'*60)
b = np.array([1, 1, 0])
m = M[:, [1, 2, 3]]
bmi = cal_bmi(b, m)
print(np.matmul(bmi, M))
