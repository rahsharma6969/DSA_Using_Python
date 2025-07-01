'''
377. Combination Sum IV
Medium
Topics
premium lock icon
Companies
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
'''

#Top-Down
def combinationSum4(nums, target):
    from functools import lru_cache

    @lru_cache(None)
    def dp(t):
        if t == 0:
            return 1
        if t < 0:
            return 0

        total = 0
        for num in nums:
            total += dp(t - num)
        return total

    return dp(target)



# Bottom-Up
def CombinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # base case: one way to make 0 — choose nothing

    for t in range(1, target + 1):
        for num in nums:
            if t - num >= 0:
                dp[t] += dp[t - num]

    return dp[target]

nums = [1,2,3]
target = 4

print(combinationSum4(nums, target))

    