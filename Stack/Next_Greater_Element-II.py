'''

Code
Testcase
Test Result
Test Result
503. Next Greater Element II
Medium
Topics
premium lock icon
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]



Approach :
stack is used to store idx of element whose next greater element hasn't been found
When we find next greater element then we update the ans for entre element
'''


    
def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):  # from 2n-1 to 0
        while stack and nums[i % n] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            res[i % n] = nums[stack[-1]]
        stack.append(i % n)

    return res
