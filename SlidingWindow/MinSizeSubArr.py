'''

Code
Testcase
Test Result
Test Result
209. Minimum Size Subarray Sum
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 '''
 
 
 #Approach:
    #1. Use a sliding window approach to find the minimal length of a subarray whose sum is greater than or equal to target.
    #2. Initialize two pointers (left and right) to represent the current window.
    #3. Expand the right pointer to include elements in the window until the sum is greater than or equal to target.
    #4. Once the sum is greater than or equal to target, move the left pointer to reduce the window size while maintaining the condition.
    #5. Keep track of the minimum length of the subarray that meets the condition.
    #6.At the end, return the minimum length found or 0 if no such subarray exists.
    
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0
        
        