'''
120. Triangle
Medium
Topics
premium lock icon
Companies
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10'''

'''Approach:
1.Given Problem is based on 2-D Array in DP
2.Here I can only move down or Down-Right'''


from functools import lru_cache
def minimalTotal(triangle):
    n = len(triangle)
    
    @lru_cache(None)
    
    def f(r,i):
        if r == n - 1:
            return triangle[r][i]
        
        return triangle[r][i]  + min(f(r + 1, i), f(r + 1, i + 1))
    
    return f(0,0)
        
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimalTotal(triangle))


# O(n^2), where n is the number of rows in 
# the triangle. Each subproblem (r, i) is computed at most once and there are O(n^2) such subproblems.