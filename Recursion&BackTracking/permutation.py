'''
46. Permutations
Solved
Medium
Topics
premium lock icon
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start):
            # Base case: if we've processed all positions
            if start == len(nums):
                result.append(nums[:])  # Copy current arrangement
                return
            
            # Try each element from start position onwards
            for i in range(start, len(nums)):
                # Swap to place nums[i] at position 'start'
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations for remaining positions
                backtrack(start + 1)
                
                # Backtrack: restore original order
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result