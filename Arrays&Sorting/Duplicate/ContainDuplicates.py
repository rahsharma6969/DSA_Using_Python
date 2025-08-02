'''
217. Contains Duplicate
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.'''

def containsDuplicates(nums):
    seen = set()  # Use a set to track seen numbers or else we can use a dictionary
    
    for num in nums:
        if num in seen:
            return True 
        seen.add(num)
        
    return False  

