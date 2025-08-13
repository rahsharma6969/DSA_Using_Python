'''

Code


Testcase
Testcase
Test Result
75. Sort Colors
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Note: It can be solved with any Sorting technique
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])

            return merge(left_half, right_half)

        def merge(left, right):
            merged = []
            i = j = 0

            # Merge elements from left and right in sorted order
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Add any remaining elements
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # Apply merge sort
        sorted_nums = merge_sort(nums)

        # Modify nums in-place
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
            


# Optimized approach

def sortColor(nums):
    
    count_freq = {}
    
    for num in nums:
        if num in nums:
            count_freq[num] += 1
        else:
            count_freq[num] = 1
            
    index = 0
    for num in range(3):  # Only 0, 1, 2
        for _ in range(count_freq[num]):
            nums[index] = num
            index += 1

#dutch National Flag :
def dutch_national_flag_sort(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# Example usage
arr = [2, 0, 1, 2, 1, 0]
print("Sorted array:", dutch_national_flag_sort(arr))

# Time complexity:
# The merge sort approach has a time complexity of O(n log n), where n is the length of nums.
# The optimized counting approach has a time complexity of O(n), since it makes two passes over the array.
# The time complexity for Dutch National Flag will be O(n), and Space complexity will be O(1) Since it does work in single pass
        
        
        
        
            
    
