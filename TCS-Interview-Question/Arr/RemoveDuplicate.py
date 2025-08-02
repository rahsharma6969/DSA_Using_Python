'''
Remove duplicates from Sorted Array
Last Updated : 19 Nov, 2024
Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

Examples: 

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
'''


def remove_duplicates(arr):
    if not arr:
        return 0
    
    new_arr = set(arr)
    return sorted(new_arr)

def Remove_duplicates(arr):
    if not arr:
        return 0

    new_arr = set(arr)         # removes duplicates
    return sorted(new_arr)     # returns sorted list of unique elements


# Example usage:
if __name__ == "__main__":
    arr = [2, 2, 2, 2, 2]
    result = remove_duplicates(arr)
    print("Distinct sorted subarray:", result)  # Output: [2]
    
    arr = [1, 1, 2, 3, 3, 4]
    result = remove_duplicates(arr)
    print("Distinct sorted subarray:", result)  # Output: [1, 2, 3, 4]
    
    