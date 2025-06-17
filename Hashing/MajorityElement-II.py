'''
229. Majority Element II
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]'''
from typing import List
def majorityElement(self, nums: List[int]) -> List[int]:
    majority_element = len(nums) // 3
    count_map = {}
    ans = []
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    for num, count in count_map.items():
        if count > majority_element:
            ans.append(num)
    return ans