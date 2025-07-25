'''
198. House Robber
Medium
Topics
premium lock icon
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 '''
 
''' Approach:
1. Create a dynamic programming array to store the maximum amount of money that can be robbed up to each house.
2. Initialize the first two elements of the array based on the first two houses.    
3.Iterate through the house arr and update the dp array based on the maximum amount that can be robbed up to that house.
4. Return the last element of the dp array, which contains the maximum amount of 
money that can be robbed without alerting the police.

Base Cases:
1.If index becomes less than 0 return 0
2. If index is 0 return nums[0]

key Idea is that if i want to rob current house then i need to know the max profit of prev two

'''

# top-down approach(memoization)

def rob(nums):
    memo = {}
    def dp(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(dp(i-1), dp(i-2) + nums[i])
        return memo[i]
    return dp(len(nums)-1)




# Bottom-up approach (tabulation)
def rob_tabulation(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])  # Store the maximum amount that can be robbed from the first two houses
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]