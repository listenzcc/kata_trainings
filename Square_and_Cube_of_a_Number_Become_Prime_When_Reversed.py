# coding: utf-8


'''The number 89 is the first positive integer that has a particular, curious property:

The square of 89 is 7921; 89² = 7921

The reverse of 7921 is 1297, and 1297 is a prime number.

The cube of 89 is 704969; 89³ = 704969

The reverse of 704969 is 969407, and 969407 is a prime number.

The first four terms of this sequence having this special property are:

n-th term      term value
    1               89 
    2              271
    3              325
    4              328
Create a function sq_cub_rev_prime(), that receives the ordinal number of the sequence and outputs its correspoding value.

Use the above table to show how the function should work:

sq_cub_rev_prime(1) == 89 
sq_cub_rev_prime(2) == 271
sq_cub_rev_prime(3) == 325
sq_cub_rev_prime(4) == 328
Your code will be tested up to the 250th term

This is not a registered sequence of OESIS, so if you are one of the first ten people that solve this kata, you may have the privilege to register the sequence at https://oeis.org, with your name. If you do so, please, mention in your biography that you are a Codewarrior.

Memoize your results to pass the tests.

Enjoy it!'''

import time


def quick_prime(m):
    prime_table = [True for _ in range(m)]
    prime_table[0] = False
    prime_table[1] = False
    prime_table[2] = True

    for j in range(2, m):
        if prime_table[j]:
            x = j+j
            while x < m:
                prime_table[x] = False
                x += j

    return [e for e in range(m) if prime_table[e]]


def is_prime(x):
    # Use fema rule to tell if x is prime.
    return pow(2, x-1, x) == 1


def reverse(x):
    return int(str(x)[::-1])


# numbers will be remembered for each test.
numbers = []


def sq_cub_rev_prime(n):
    # your code here
    # x is the n-th term of the sequence

    x = numbers[-1] + 1 if numbers else 89
    while len(numbers) < n:
        if is_prime(reverse(x ** 2)) and is_prime(reverse(x ** 3)):
            numbers.append(x)
        x += 1

    return numbers[n-1]


print(sq_cub_rev_prime(3))
