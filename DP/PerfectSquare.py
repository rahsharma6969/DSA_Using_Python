'''
279. Perfect Squares
Medium
Topics
premium lock icon
Companies
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.'''


def numSquares(n):
    df = [float('inf')] * (n + 1)
    
    def perfectSquares():
        squares = []
        
        while len(squares) * len(squares) <= n:
            squares.append(len(squares) * len(squares))
        return squares
    squares = perfectSquares()
    df[0] = 0  # 0 perfect squares to make 0
    
import math

def NumSquares(n):
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    
    min_count = float('inf')
    for i in range(1, int(math.isqrt(n)) + 1):
        square = i * i
        result = numSquares(n - square)
        min_count = min(min_count, 1 + result)
    
    return min_count


import math

def numSquares(n):
    memo = {}

    def minSquares(k):
        if k == 0:
            return 0
        if k in memo:
            return memo[k]

        min_count = float('inf')
        for i in range(1, int(math.isqrt(k)) + 1):
            square = i * i
            res = minSquares(k - square)
            min_count = min(min_count, 1 + res)
        
        memo[k] = min_count
        return min_count

    return minSquares(n)


    