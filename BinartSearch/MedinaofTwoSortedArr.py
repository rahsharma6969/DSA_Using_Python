'''
4. Median of Two Sorted Arrays
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 '''
 
 
# def findMedianSortedArrays(nums1, nums2):
#     m, n = len(nums1), len(nums2)
    
#     nums = nums1 + nums2
#     nums.sort()
    
#     mid = (m + n) // 2
    
#     if (m + n) % 2 == 0:
#         return (nums[mid - 1] + nums[mid]) / 2
#     else:
#         return nums[mid]
# Time Complexity O((m+n) log(m+n)) due to sorting the combined array.  


def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = total_left - i

        nums1_left = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right = float('inf') if i == m else nums1[i]
        nums2_left = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right = float('inf') if j == n else nums2[j]

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if (m + n) % 2 == 0:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            else:
                return max(nums1_left, nums2_left)
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1 
    
# Example usage
nums1 = [1, 3]  
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
        # End of the second half
     