# code: utf-8


def solution(a):
    n = len(a)
    a = set(_ for _ in a)
    while True:
        print(a)
        if len(a) == 1:
            return a.pop() * n
        m = min(a)
        a = set(mm(_, m) for _ in a)


def mm(x, m):
    x %= m
    if x == 0:
        x += m
    return x


test1 = [9]
test2 = [6, 9, 21]
test3 = [1, 21, 55]
test4 = [4, 16, 24]

print(solution(test1))
print(solution(test2))
print(solution(test3))
print(solution(test4))
