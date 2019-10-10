# coding: utf-8

''' It seems primes_under_0 is fastest '''
import time


def primes_under_0(n_max):
    primes = set()
    ignores = [False for _ in range(n_max)]
    for e in range(2, n_max):
        if ignores[e]:
            continue
        primes.add(e)
        j = e
        while j < n_max:
            ignores[j] = True
            j += e
    return primes


def primes_under_1(n_max):
    primes = set()
    ignores = {e: False for e in range(n_max)}
    for e in range(2, n_max):
        if ignores[e]:
            continue
        primes.add(e)
        j = e
        while j < n_max:
            ignores[j] = True
            j += e
    return primes


n_max = 100000
n = 10

print(primes_under_0(100))
print(primes_under_1(100))

t = time.time()
for _ in range(n):
    primes_under_0(n_max)
print(time.time()-t)

t = time.time()
for _ in range(n):
    primes_under_1(n_max)
print(time.time()-t)
