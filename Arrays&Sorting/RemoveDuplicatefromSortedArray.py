'''
26. Remove Duplicates from Sorted Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:'''

def removeDuplicates(nums):
    if not nums:
        return 0
    dup_nums  = set(nums)  # Using set to remove duplicates
    print(f"Unique elements found: {dup_nums}")
    nums[:] = sorted(dup_nums)  # Sort the unique elements
    return len(nums)


# Example usage
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4]
    k = removeDuplicates(nums)
    print(f"Number of unique elements: {k}")
    print(f"Modified array: {nums[:k]}")
    