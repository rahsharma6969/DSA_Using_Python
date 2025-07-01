'''

Code
Testcase
Test Result
Test Result
673. Number of Longest Increasing Subsequence
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1,
and there are 5 increasing subsequences of length 1, so output 5.
'''

def findNumberOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    length = [1] * n   # LIS length ending at i
    count = [1] * n    # number of LIS ending at i

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)

    return sum(c for l, c in zip(length, count) if l == max_len)

            
            
        