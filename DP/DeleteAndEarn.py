'''
740. Delete and Earn
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.'''

#Approach:
# 1. Create a frequency array to count occurrences of each number.
# 2. Use dynamic programming to calculate the maximum points.
#3. For Each Number i, calculate the maximum points by either taking it (and skipping i-1) or skipping it.
#4. The recurrence relation can be defined as:
# max_points[i] = max(max_points[i-1], max_points[i-2]) + i * freq[i]
#5. The base cases are:
# max_points[0] = 0 (no points for number 0)
# max_points[1] = freq[1] * 1 (points for number 1 based on its frequency)
#6. The final answer will be in max_points[max_num], where max_num is the maximum number in the input array.



# Using Dynamic Programming to solve the problem
def deleteAndEarn(nums):
    if not nums:
        return 0
    max_num = max(nums)
    freq = [0] * (max_num + 1) 
    for num in nums:
        freq[num] += 1
    dp = [0] * (max_num + 1)
    dp[1] = freq[1] * 1 
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + freq[i] * i)
    return dp[max_num]


# Using Recursion with Memoization to solve the problem
def deleteAndEarnMemo(nums):
    if not nums:
        return 0
    max_num = max(nums)  # Get the maximum number in the input array
    freq = [0] * (max_num + 1)  # Create a frequency array to count occurrences of each number
    for num in nums:  # Count the frequency of each number
        freq[num] += 1

    memo = {}

    def dp(i):
        if i <= 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(dp(i - 1), dp(i - 2) + freq[i] * i)  # Calculate the maximum points for number i
        return memo[i]

    return dp(max_num)

# Example usage:
nums = [3, 4, 2, 2, 3, 3, 4]
print(deleteAndEarnMemo(nums))  # Output: 6
