'''
977. Squares of a Sorted Array
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
'''

# Brute force approach to square and sort the array
def sortedSquares(nums):
    n = len(nums)
    
    for i in range(n):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums

# Two pointers approach to square and sort the array
def sortedSquaresTwoPointers(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    
    for i in range(n - 1, -1, -1): # Start from the end of the result array
        if abs(nums[left]) > abs(nums[right]):  # Compare absolute values
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
            
    return result

# Example usage
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]

    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))  # Output: [4, 9, 9, 49, 121]