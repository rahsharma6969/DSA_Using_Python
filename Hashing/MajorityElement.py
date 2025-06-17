'''
169. Majority Element
Solved
Easy
Topics
premium lock icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 '''
 
def majorityElement(nums):
    majority_count = len(nums) // 2
    count_map = {}
     
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
             
    for num, count in count_map.items():
        if count > majority_count:
            return num
    return None  # In case no majority element is found, though the problem guarantees one exists
 
#Example usage
nums = [3, 2, 3]
result = majorityElement(nums)
print(f"The majority element in {nums} is: {result}")
# Example usage with another input
nums2 = [2, 2, 1, 1, 1, 2, 2]