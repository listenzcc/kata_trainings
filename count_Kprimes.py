#code: utf-8


def count_Kprimes(k, start, end):
    return [n for n in range(start, end+1) if find_k(n) == k]


def puzzle(s):
    a = count_Kprimes(1, 0, s)
    b = count_Kprimes(3, 0, s)
    c = count_Kprimes(7, 0, s)

    return sum(1 for x in a for y in b for z in c if x + y + z == s)


def find_k(n):
    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            res += 1
        i += 1
    if n > 1:
        res += 1
    return res


count_Kprimes(3, 0, 100)
