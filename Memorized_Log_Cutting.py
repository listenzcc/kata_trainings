# coding: utf-8

'''
CLEAR CUTTER'S NEEDS YOUR HELP!
The logging company Clear Cutter's makes its money by optimizing the price-to-length of each log they cut before selling them. An example of one of their price tables is included:

# So a price table p
p = [ 0,  1,  5,  8,  9, 10]

# Can be imagined as:
# length i | 0  1  2  3  4  5 *in feet*
# price pi | 0  1  5  8  9 10 *in money*
They hired an intern last summer to create a recursive function for them to easily calculate the most profitable price for a log of length n using price table p as follows:

def cut_log(p, n):
   if (n == 0):
      return 0
   q = -1
   for i in range(1, n+1)
      q = max(q, p[i] + cut_log(p, n-i))
   return q
An example of the working code:

cut_log(p, 5) # => 13
# 5ft = $10, BUT 2ft + 3ft = 5ft -> $5 + $8 = $13 which is greater in value
However, their senior software engineer realized that the number of recursive calls in the function gives it an awful running time of 2^n (as this function iterates through ALL 2^n-1 possibilities for a log of length n).

Having discovered this problem just as you've arrived for your internship, he responsibly delegates the issue to you.

Using the power of Stack Overflow and Google, he wants you to create a solution that runs in ¦¨(n^2) time so that it doesn't take 5 hours to calculate the optimal price for a log of size 50. (He also suggests to research the problem using the keywords in the tags)

(Be aware that if your algorithm is not efficient, it will attempt to look at 2^49 = 562949953421312 nodes instead of 49^2 = 2401... The solution will automatically fail if it takes longer than 6 seconds... which occurs at right around Log 23)
'''

##############################################################
# A good example of dynamic programming

import time
###############################################################
#    0    1    2    3    4    5    6    7... and so on
p = [0,   1,   5,   8,   9,  10,  17,  17,  20,  24,  # 0X's
     30,  32,  35,  39,  43,  43,  45,  49,  50,  54,  # 1X's
     57,  60,  65,  68,  70,  74,  80,  81,  84,  85,  # 2X's
     87,  91,  95,  99, 101, 104, 107, 112, 115, 116,  # 3X's
     119]  # 40th element


def cut_log(p, n):
    # solutions is dynamic programming of the current max price of the n-length log.
    # Use list to store solutions
    solutions = [0 for _ in range(max(len(p), n+1))]
    # init
    for j in range(len(solutions)):
        if j < len(p):
            solutions[j] = p[j]
    # dynamic
    for j in range(n):
        for k in range(n):
            # if j+k is too large, we are not interested.
            if j+k < n+1:
                solutions[j+k] = max(solutions[j+k], solutions[j]+solutions[k])

    return solutions[n]


def cut_log1(p, n):
    # Use dict to store solutions
    solutions = dict()
    # init
    for j, pi in enumerate(p):
        solutions[j] = pi
    # dynamic
    for j in range(n):
        for k in range(n):
            # if j+k is too large, we are not interested.
            if j+k > n:
                continue
            # incase solutions has not j+k yet
            if j+k not in solutions.keys():
                solutions[j+k] = 0
            solutions[j+k] = max(solutions[j+k], solutions[j]+solutions[k])

    return solutions[n]


def cut_log_slow(p, n):
    if (n == 0):
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_log_slow(p, n-i))
    return q


for n in [5, 8, 10, 22, 50]:
    print('-' * 80)

    # run and timing cut_log, it is faster
    t = time.time()
    print(cut_log(p, n))
    for j in range(100):
        cut_log(p, n)
    print(time.time() - t)

    # run and timming cut_log1, it is slower
    t = time.time()
    print(cut_log1(p, n))
    for j in range(100):
        cut_log1(p, n)
    print(time.time() - t)

    if n > 20:
        continue
    # run and timming cut_log_slow,
    # it is really slow.
    t = time.time()
    print(cut_log_slow(p, n))
    for j in range(100):
        cut_log_slow(p, n)
    print(time.time() - t)
