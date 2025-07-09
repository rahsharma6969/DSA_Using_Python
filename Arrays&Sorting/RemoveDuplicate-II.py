'''
80. Remove Duplicates from Sorted Array II
Medium
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.'''


def removeDuplicates(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
         return len(nums)
    write = 2
    for read in range(2, len(nums)):   # Since starting from index 2, we can check for duplicates
        if nums[read] != nums[write - 2]: # We check if the current number is not equal to the number at write - 2
            nums[write] = nums[read]      # If it's not a duplicate, we write it at the current write index
            write += 1  
    return write
        

# Example usage:
nums = [0,0,1,1,1,1,2,3,3]
k = removeDuplicates(nums)
print(k)  # Output: 5
        
    
        
        