'''
16. 3Sum Closest
Medium
Topics
premium lock icon
Companies
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).'''

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')  # or use a large number like 1e9

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            # Update closest_sum if needed
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            # Move pointers
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:  # Exact match
                return curr_sum

    return closest_sum


nums = [-1,2,1,-4]

print(threeSumClosest(nums, 2))