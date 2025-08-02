'''
Rotate an Array by d - Counterclockwise or Left
Last Updated : 03 Oct, 2024
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
'''

def rotate_array(arr, d):
    
    while d > 0:
        d -= 1
        element = arr[0]
        arr.pop(0)
        arr.append(element)
    return arr

def Rotate_array(arr, d):
    d = d % len(arr)  # handle d > len(arr)
    return arr[d:] + arr[:d]

      
# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    result = rotate_array(arr, d)
    print("Rotated array:", result)  # Output: [3, 4, 5, 6, 1, 2]