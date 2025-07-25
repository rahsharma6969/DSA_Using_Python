'''
213. House Robber II
Medium
Topics
premium lock icon
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3'''

def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    def rob_linear(arr):
        m = len(arr)
        dp = [0] * m
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, m):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        return dp[-1]

    # Two scenarios: exclude last house or exclude first house
    return max(
        rob_linear(nums[:-1]),  # rob houses 0 to n-2
        rob_linear(nums[1:])    # rob houses 1 to n-1
    )
