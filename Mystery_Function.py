# -*- coding: utf-8 -*-

# Mystery Function
# 4kyu
# Gray code

'''
The mystery function is defined over the non-negative integers. The more common name of this function is concealed in order to not tempt you to search the Web for help in solving this kata, which most definitely would be a very dishonorable thing to do.

Assume num has n bits. Then mystery(num) is the number whose binary representation is the numth entry in the table T(n), where T(n) is defined recursively as follows:

T(1) = [0, 1]
T(n + 1) is obtained by taking two copies of T(n), reversing the second copy, prepending each entry of the first copy with 0 and each entry of the reversed copy with 1, and then concatenating the two. For example:

T(2) = [ 00, 01, 11, 10 ]
and

T(3) = [ 000, 001, 011, 010, 110, 111, 101, 100 ]
mystery(6) is the 6th entry in T(3) ( with indexing starting at 0 ), i.e., 101 interpreted as a binary number. So, mystery(6) returns 5.

Your mission is to implement the function mystery, where the argument may have up to 63 bits. Note that T(63) is far too large to compute and store, so you'll have to find an alternative way of implementing mystery. You are also asked to implement mystery_inv ( or mysteryInv ), the inverse of mystery. Finally, you are asked to implement a function name_of_mystery ( or nameOfMystery ), which shall return the name that mystery is more commonly known as. After passing all tests you are free to learn more about this function on Wikipedia or another place.

Hint: If you don't know the name of mystery, remember there is information in passing as well as failing a test.
'''

table = [['0', '1'], ['1', '0']]

def mystery(n):
    print('-' * 80)
    m = int(n ** 0.5) + 1
    print('%d-th in T(%d)' % (n, m))

    serial = []
    n2 = n
    while n2:
        serial.append(table[(n2 // 2) % 2][n2 % 2])
        n2 //= 2
    serial.reverse()

    print(int(''.join(serial), 2))

    pass


def mystery_inv(n):
    print('-' * 80)
    idx = 0
    for e in bin(n)[2:]:
        if (idx % 2) == 0:
            if e == '1':
                idx = idx * 2 + 1
            else:
                idx = idx * 2
        else:
            if e == '1':
                idx = idx * 2
            else:
                idx = idx * 2 + 1
        # print(e, '->', idx)
    print(idx)

    pass


def name_of_mystery(n):
    pass


mystery(6)
mystery(9)
mystery(19)

mystery_inv(5)
mystery_inv(13)
mystery_inv(26)