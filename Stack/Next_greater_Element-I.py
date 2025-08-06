'''
496. Next Greater Element I
Solved
Easy
Topics
premium lock icon
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

The stack only stores indices of elements for which we haven’t yet found the next greater.

Whenever a larger number comes, it is the answer for all smaller numbers before it (from top of the stack).

Each element is pushed and popped at most once → O(n).'''

from typing import List
# 6  8  0  1  3

def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater_map = {}

    # Iterate nums2 in reverse
    for num in reversed(nums2):
        # Maintain monotonic decreasing stack
        while stack and stack[-1] <= num:
            stack.pop()

        # If stack is not empty, top is next greater
        if stack:
            next_greater_map[num] = stack[-1]
        else:
            next_greater_map[num] = -1

        # Push current num to stack
        stack.append(num)

    # Build result for nums1 using the map
    return [next_greater_map[num] for num in nums1]





    
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater_map = {}

    for num in nums2:
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater_map[prev] = num
        stack.append(num)

    # For remaining elements in stack, no greater element exists
    for remaining in stack:
        next_greater_map[remaining] = -1

    # Build result for nums1
    return [next_greater_map[num] for num in nums1]
