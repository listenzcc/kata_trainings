# coding: utf-8

'''An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].

Write a function named partitions which returns the number of integer partitions of n. The function should be able to find the number of integer partitions of n for n as least as large as 100.'''

from pprint import pprint


def partitions(n):
    # Make DP matrix
    # dp[j][k] means the sum is j and elements are not larger than k
    dp = [[0 for _ in range(n)] for __ in range(n)]

    # Init first column and diagonal elements as 1
    # Since N = N and N = sum([1, 1, ..., 1])
    for j in range(n):
        dp[j][0] = 1
        dp[j][j] = 1

    # Start dynamic programming
    # For each column
    for k in range(1, n):
        # For rows in downside of the diagonal
        for j in range(k, n):
            if j == k:
                # For elements in diagonal, add its left hand
                dp[j][k] += dp[j][k-1]
            else:
                # For others, add its left hand plus
                # max number of partitions with elements are not larger than k
                # max(dp[j-k-1][:k+1])
                # j-k-1 equals to j-(k+1)
                # means from jth row down on k rows, -1 is because k starts on 0
                # :k+1 means selecting the first k elements on this row
                dp[j][k] += dp[j][k-1] + max(dp[j-k-1][:k+1])

    # Print the DP matrix
    pprint(dp)

    # Last value is the answer.
    return dp[-1][-1]


print(partitions(5))
print(partitions(10))
